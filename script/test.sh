export PYTHONPATH='.'
export PYTHONENV='test'

export SECRET_KEY='VkGE7lKTaemghlDP'
export DATABASE_URI='postgresql://drhades:SoyEzequielEnSql@localhost/neobank_test'
pytest -s -vvvv $1 $2
