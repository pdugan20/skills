import Charts
import SwiftUI

struct ReportsView: View {
    let transactions: [Transaction]

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 24) {
                    Text("Spending by category").font(.headline)
                    Chart(transactions) { transaction in
                        BarMark(
                            x: .value("Category", transaction.category),
                            y: .value("Amount", Double(transaction.amountCents) / 100)
                        )
                        .foregroundStyle(by: .value("Category", transaction.category))
                    }
                    .frame(height: 220)
                    Text("Daily activity").font(.headline)
                    Chart(transactions) { transaction in
                        LineMark(
                            x: .value("Date", transaction.date),
                            y: .value("Amount", Double(transaction.amountCents) / 100)
                        )
                        PointMark(
                            x: .value("Date", transaction.date),
                            y: .value("Amount", Double(transaction.amountCents) / 100)
                        )
                    }
                    .frame(height: 220)
                }
                .padding()
            }
            .navigationTitle("Reports")
        }
    }
}
