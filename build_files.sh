echo " BUILD START "
python3.11 pip install -r requirements.txt
python3.11 manage.py collectstatic --noinout  --clear
echo " BUILD END "