import SwiftUI

struct RootView: View {
    @State private var transactions = SampleData.transactions

    var body: some View {
        TabView {
            TransactionListView(transactions: transactions)
                .tabItem { Label("Activity", systemImage: "list.bullet") }
            BudgetSummaryView(transactions: transactions)
                .tabItem { Label("Budgets", systemImage: "chart.pie") }
            ReportsView(transactions: transactions)
                .tabItem { Label("Reports", systemImage: "chart.bar") }
        }
    }
}

enum SampleData {
    static let transactions: [Transaction] = (0..<24).map { index in
        Transaction(
            id: UUID(),
            date: Date(timeIntervalSince1970: 1_790_000_000 + Double(index) * 86_400 * 9),
            amountCents: 1_250 + index * 337,
            category: ["Groceries", "Transit", "Dining", "Utilities"][index % 4],
            memo: "Sample \(index)"
        )
    }
}
