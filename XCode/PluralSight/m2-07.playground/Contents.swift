// Using Optionals

var regularInt: Int
var optionalInt: Int?

// can set values
regularInt = 100
optionalInt = 100

// optional binding
if let unwrappedInt = optionalInt {
    print(unwrappedInt)
}

// Check for nil
//if optionalInt != nil {
//    // force unwrapping
//    var unwrappedInt = optionalInt! //unwrapped optional
//}
