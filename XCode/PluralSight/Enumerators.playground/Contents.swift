// Enumerations

var itemTitle = "Middlemarch"

enum MediaType {
    case book(String)
    case movie(String)
    case music(Int)
    case game
}

var itemType: MediaType
itemType = .movie("Comedy")

switch itemType {
case .movie:
    print("I've been watching \(itemTitle)")
case .music:
    print("I've been listening to \(itemTitle)")
case .book:
    print("I've been reading \(itemTitle)")
case .game:
    print("I've been playing \(itemTitle)")
}
