class House:
    def __init__(self,location,house_type,deal_type,price,completion_year):
        self.location=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year

    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location,self.house_type,self.deal_type,self.price,self.completion_year))


H1=House("강남","아파트","매매","10억","2010년")
H2=House("마포","오피스텔","전세","5억","2007년")
H3=House("송파","빌라","월세","500/50","2000년")


H1.show_detail()
H2.show_detail()
H3.show_detail()
