FROM jupyter/minimal-notebook:6d42503c684f

RUN  pip install lark-parser==0.9.0 \
                 astpretty==2.0.0  \
                 more-itertools==8.5.0  \
                 funcy==1.14 \
     && fix-permissions $CONDA_DIR \
     && fix-permissions /home/$NB_USER
     
RUN echo 'export PATH="$PATH:$HOME/bin"' >> $HOME/.bashrc
