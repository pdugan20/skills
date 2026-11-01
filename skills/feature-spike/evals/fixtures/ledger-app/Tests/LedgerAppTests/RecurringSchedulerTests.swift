import Foundation
import Testing

@testable import LedgerApp

@Test func quarterlyScheduleAddsThreeMonths() {
    var calendar = Calendar(identifier: .gregorian)
    calendar.timeZone = TimeZone(identifier: "UTC") ?? .current
    let start = Date(timeIntervalSince1970: 1_790_000_000)
    let dates = RecurringScheduler(calendar: calendar).occurrences(startingOn: start, everyMonths: 3, count: 4)
    #expect(dates.count == 4)
    #expect(calendar.dateComponents([.month], from: dates[0], to: dates[3]).month == 9)
}
