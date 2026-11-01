import Foundation

struct Transaction: Identifiable, Equatable, Sendable {
    let id: UUID
    let date: Date
    let amountCents: Int
    let category: String
    let memo: String
}
