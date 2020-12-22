class Boxplot:
    """
    class for bokeh boxplot
    input: pandas dataframe with value and group by column
    """
    
    def __init__(self, df, value, by): 
        self.df = df
        self.value = value
        self.by = by
        self.groups = self.df.groupby(by)
        self.q1 = self.groups.quantile(q=0.25)
        self.q2 = self.groups.quantile(q=0.5)
        self.q3 = self.groups.quantile(q=0.75)     
        self.out = []
        self.outx = []
        self.outy = []
        self.qmin = self.groups.quantile(q=0.00)
        self.qmax = self.groups.quantile(q=1.00) 

    
    @property
    def iqr(self):
        return self.q3 - self.q1
    
    @property
    def upper(self):
        return self.q3 + 1.5*self.iqr
    
    @property
    def lower(self):
        return self.q1 - 1.5*self.iqr
    
    def __outliers__(self, g):
        cat = g.name
        g = g[(g[self.value] > self.upper.loc[cat][self.value]) | 
              (g[self.value] < self.lower.loc[cat][self.value])][self.value]
        return g
    
    def get_outliers(self):
        self.out = self.groups.apply(self.__outliers__).dropna()
        if not self.out.empty:
            for keys in self.out.index:
                self.outx.append(keys[0])
                self.outy.append(self.out.loc[keys[0]].loc[keys[1]])

            
    def set_minmax(self):
       #if no outliers, shrink lengths of stems to be no longer than the minimums or maximums
        self.upper[self.value]= [min([x,y]) for (x,y) in zip(list(self.qmax.loc[:,self.value]),self.upper[self.value])]
        self.lower[self.value] = [max([x,y]) for (x,y) in zip(list(self.qmin.loc[:,self.value]),self.lower[self.value])]
                
    def __str__(self):
        return f"q1: {self.q1}\nq3: {self.q3}\niqr: {self.iqr}"
    
    def boxplot(self, segment_color = "black", vfillcolor = "grey", 
             outcolor = "red", height = 400, width = 400):
        self.get_outliers()
        self.set_minmax()
        cats = sorted(self.df[self.by].unique())
        
        p = figure(tools="", 
                   background_fill_color="#efefef", 
                   x_range=cats, 
                   toolbar_location=None,
                   plot_width=width, 
                   plot_height=height, 
                   title = f"boxplot of {self.value} grouped by {self.by}")

        # stems
        p.segment(cats, 
                  self.upper[self.value], 
                  cats, 
                  self.q3[self.value], 
                  line_color=segment_color)
        p.segment(cats, 
                  self.lower[self.value], 
                  cats, 
                  self.q1[self.value], 
                  line_color=segment_color)

        # boxes
        p.vbar(cats, 
               0.7, 
               self.q2[self.value], 
               self.q3[self.value], 
               fill_color=vfillcolor, 
               line_color="black")
        p.vbar(cats, 
               0.7, 
               self.q1[self.value], 
               self.q2[self.value], 
               fill_color=vfillcolor, 
               line_color="black")

        # whiskers (almost-0 height rects simpler than segments)
        p.rect(cats, 
               self.lower[self.value], 
               0.2, 
               0.01, 
               line_color="black")
        p.rect(cats, 
               self.upper[self.value], 
               0.2, 
               0.01, 
               line_color="black")

        # outliers
        if not self.out.empty:
            p.circle(self.outx, self.outy, size=6, color=outcolor, fill_alpha=0.6)

        p.xgrid.grid_line_color = None
        p.ygrid.grid_line_color = "white"
        p.grid.grid_line_width = 2
        p.xaxis.major_label_text_font_size="10px"

        return p