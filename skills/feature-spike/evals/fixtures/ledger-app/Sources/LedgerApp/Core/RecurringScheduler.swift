import Foundation

/// Expands a recurring transaction into its upcoming dates.
struct RecurringScheduler: Sendable {
    let calendar: Calendar

    func occurrences(startingOn start: Date, everyMonths months: Int, count: Int) -> [Date] {
        (0..<count).compactMap { calendar.date(byAdding: .month, value: $0 * months, to: start) }
    }
}
