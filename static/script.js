document.addEventListener("DOMContentLoaded", function () {
    loadExpenses();

    const form = document.getElementById("expense-form");
    form.addEventListener("submit", function (e) {
        e.preventDefault();
        const formData = new FormData(form);
        fetch("/add", {
            method: "POST",
            body: formData,
        })
        .then((res) => res.json())
        .then((data) => {
            if (data.status === "success") {
                form.reset();
                loadExpenses();
            }
        });
    });
});

function loadExpenses() {
    fetch("/expenses")
        .then((res) => res.json())
        .then((data) => {
            const tbody = document.getElementById("expenses-body");
            tbody.innerHTML = "";

            data.forEach((expense) => {
                const [id, date, amount, category, note] = expense;
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${date}</td>
                    <td>₹${amount}</td>
                    <td>${category}</td>
                    <td>${note}</td>
                    <td><button onclick="deleteExpense(${id})">Delete</button></td>
                `;
                tbody.appendChild(row);
            });
        });
}

function deleteExpense(id) {
    fetch(`/delete/${id}`, {
        method: "POST",
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.status === "deleted") {
            loadExpenses();
        }
    });
}
