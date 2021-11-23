# BFVM19PROG1
Programming 1 course for DSLS

see also https://fennaf.gitbook.io/bfvm19prog1/


# Install on your own system
Run the following code in your terminal (using a prefered virtual environmnent name)

```
#create virtual environment
virtualenv -p /usr/bin/python3 {name}
source {name}/bin/activate
#create jupyter notebook kernel for venv
pip install ipykernel
python -m ipykernel install --user --name={name}
#install required packages
pip install numpy
pip install pandas
pip install matplotlib
```

#run jupyter notebook
```
jupyter notebook
```
after running the notebook select the just created kernel
