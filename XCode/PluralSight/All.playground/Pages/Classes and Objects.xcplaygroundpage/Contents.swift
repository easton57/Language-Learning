// Defining and Instantiating Classes

class Appliance {
    // properties
    var manufacturer: String
    var model: String
    var voltage: Int
    var capacity: Int?
    
    // initializer
    init() {
        self.manufacturer = "default manufacturer"
        self.model = "default model"
        self.voltage = 120
    }
    
    // additional initalizier
    init(withVoltage: Int) {
        self.manufacturer = "default manufacturer"
        self.model = "default model"
        self.voltage = withVoltage
    }
    
    deinit {
        // perform cleanup code
        // release a file
    }
    
    // methods
    func getDetails() -> String {
        var message = "This is the \(self.model) from \(self.manufacturer)."
        if self.voltage >= 220 {
            message += "This model is for European usage."
        }
        return message
    }
}

var cafetiere = Appliance(withVoltage: 220)
cafetiere.manufacturer = "Megappliance EU"
cafetiere.model = "Electrotiere"
print(cafetiere.getDetails())

// ...later, creat an instance of Appliance
var kettle = Appliance()
kettle.manufacturer = "Megappliance, Inc"
kettle.model = "TeaMaster 5000"
kettle.voltage = 120
print(kettle.getDetails())
