from sqlalchemy import create_engine, MetaData


engine = create_engine('mysql+pymysql://turing:0623@turing.kro.kr:3306/yolo')
meta = MetaData()
conn = engine.connect()
