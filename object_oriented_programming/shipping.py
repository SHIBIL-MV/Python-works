# expres shipping =>cweight*5

#standardshipping =>cweight*10

class shipping:

    def calculate_shipping_cost(self,weight):

        print(weight*5)

class expressshipping(shipping):

    def calculate_shipping_cost(self, weight):

        print(weight*20)

class standardshipping(shipping):

    def calculate_shipping_cost(self, weight):

        print(weight*10)

expe_instance=expressshipping()

expe_instance.calculate_shipping_cost(10)

std_instance=standardshipping()

std_instance.calculate_shipping_cost(10)

