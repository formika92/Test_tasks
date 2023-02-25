from dataclasses import dataclass

technic = [('Ноутбук', 1500, 'Татьяна', '89002001020'),
           ('Смартфон', 500, 'Анна', '89202202325'),
           ('Проектор ', 300, 'Андрей', '89505205656'),
           ('Принтер', 750, 'Игорь', '89303303236'),
           ('Планшет', 2300, 'Игорь', '89303303236'),
           ('Смартфон', 1000, 'Андрей', '89505205656'),
           ('Ноутбук', 4800, 'Татьяна', '89002001020'),
           ('Наушники', 780, 'Марина', '89562002350'),
           ('Сканер', 550, 'Сергей', '89808564559'),
           ('Планшет', 1200, 'Анна', '89202202325'),
           ('Ноутбук', 1100, 'Игорь', '89303303236'),
           ('Смартфон', 3500, 'Татьяна', '89002001020')]


@dataclass
class Client:
    name: str
    phone: str

    def __str__(self):
        return f"{self.name} {self.phone}"

    def __hash__(self):
        return hash(self.name)


@dataclass
class Order:
    name: str
    price: int

    def __str__(self):
        return f"{self.name} - {self.price}"


class ClientOrders(dict):

    def __str__(self):
        s = ''
        for client, orders in self.items():
            o = ''
            for order in orders:
                o += f'{str(order)}; '
            s += f"{str(client)}: {o}\n"
        return s

    def add_new_order(self, order: Order, client: Client) -> None:
        orders = self.get(client)
        if orders:
            orders.append(order)
        else:
            orders = [order]
        self[client] = orders

# or can create an entity of the form
# ClientOrder:
#   client: Client
#   orders: List[Order]
# store entities in a list/set, in a dictionary as values


def prepare_dict() -> ClientOrders:
    client_orders = ClientOrders()
    for order in technic:
        tech, price, client_name, client_phone = order
        client_orders.add_new_order(
            Order(name=tech, price=price),
            Client(name=client_name, phone=client_phone)
        )

    return client_orders
