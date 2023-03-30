import datetime
import json
if __name__=="__main__":
    dt = datetime.datetime(2023,3,29,18,30,43,295000,tzinfo=datetime.timezone.utc);
print(dt);
str = dt.strftime('YY-mm-DD');

json.dumps(str);

datetime.datetime(2023,3,29,18,30,43,295000,tzinfo=datetime.timezone.utc)
