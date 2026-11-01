import Foundation

/// App-wide settings read by views and, for historical reasons, by budgeting logic.
@MainActor
final class AppEnvironment {
    static let shared = AppEnvironment()

    var calendar: Calendar
    var currencyCode = "USD"

    var currencyFormatter: NumberFormatter {
        let formatter = NumberFormatter()
        formatter.numberStyle = .currency
        formatter.currencyCode = currencyCode
        formatter.locale = Locale(identifier: "en_US")
        return formatter
    }

    private init() {
        var calendar = Calendar(identifier: .gregorian)
        calendar.timeZone = TimeZone(identifier: "UTC") ?? .current
        self.calendar = calendar
    }
}
