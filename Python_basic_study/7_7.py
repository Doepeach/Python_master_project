#남자:키*키*22
#여자:키*키*21

def std_weight(height,gender):
    if gender=="남자":
        new_weight=round(height*height*22/10000,2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height,new_weight))
    elif gender=="여자":
        new_weight=round(height*height*21/10000,2)
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height,new_weight))

std_weight(175,"남자")
