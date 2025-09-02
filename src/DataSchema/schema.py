from pydantic import BaseModel,Field
from typing import Annotated,Literal

"""
<class 'pandas.core.frame.DataFrame'>
Index: 1316 entries, 0 to 1318
Data columns (total 7 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   Age                       1316 non-null   int64  
 1   Gender                    1316 non-null   int64  
 2   Heart rate                1316 non-null   int64  
 3   Systolic blood pressure   1316 non-null   int64  
 4   Diastolic blood pressure  1316 non-null   int64  
 5   Blood sugar               1316 non-null   float64
 6   Result                    1316 non-null   object 
dtypes: float64(1), int64(5), object(1)
"""
class Patient(BaseModel):
    Age: Annotated[int, Field(..., ge=0, le=120)]  # age between 0 and 120
    Gender: Literal[0, 1]  # 0 for female, 1 for male
    Heart_rate: Annotated[int, Field(..., ge=30, le=200)]
    Systolic_blood_pressure: Annotated[int, Field(..., ge=20, le=250)]
    Diastolic_blood_pressure: Annotated[int, Field(..., ge=10, le=150)]
    Blood_sugar: Annotated[float, Field(..., ge=0)]