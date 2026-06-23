class Train:
    def __init__(self,name,line,avarage_speed,quality,ticket_cost,capacity):
        self.id = 1
        self.name = name
        self.line = line
        self.avarage_speed = avarage_speed
        self.quality = quality
        self.ticket_cost= ticket_cost
        self.capacity = capacity
    def __str__(self):
        return f"Name: {self.name}\nLine: {self.line}\nAvarage_speed: {self.avarage_speed}\nQuality: {self.quality}\nticket_cost: {self.ticket_cost}\nCapacity: {self.capacity}\n"

