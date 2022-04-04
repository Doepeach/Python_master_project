class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5) # 체력 80, 공격력 5
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 멤버변수 접근

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.cloaking = True # 빼앗은 레이스만을 위한 특별한 멤버변수 정의

if wraith2.cloaking == True: # 클로킹 상태라면?
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# 에러 발생
# if wraith1.cloaking == True: # 우리가 만든 레이스 클로킹 여부
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith1.name))
 