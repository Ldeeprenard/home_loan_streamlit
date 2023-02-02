# app/Dockerfile

FROM python:3.9-slim


WORKDIR C:\Users\Lrenard\Documents\openclassroom\projet 7\streamlit\home_loan_streamlit
copy requirements.txt ./requirements.txt
run pip3 install -r requirements.txt

EXPOSE 8501
copy Accueil.py ./Accueil.py
copy pages ./pages
copy clients_test.csv ./clients_test.csv
copy colonnes_home_loan.joblib ./colonnes_home_loan.joblib
ENTRYPOINT ["streamlit", "run"]
CMD ["Accueil.py"]