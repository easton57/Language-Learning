// Inheritance
class Appliance {
    var make: String
    var model: String
    init() {
        self.make = "default"
        self.model = "default"
    }
    final func printDetails() {
        print("Make: \(self.make) \nModel: \(self.model)")
    }
}

// define a new class
class Toaster: Appliance {
    // new properties
    var slices: Int
    
    override init() {
        self.slices = 2
        super.init()
    }
    // new method
    func toast() {
        print("Irradiating now...")
    }
}

var myToaster = Toaster()
myToaster.make = "AcmeCorp"
myToaster.model = "Carbonizer"
myToaster.printDetails()
myToaster.toast()
