async function fetchEmployees() {
    const role = document.getElementById("role").value;
    const location = document.getElementById("location").value;
    const includeInactive = document.getElementById("inactive").checked;

    const res = await fetch(`http://127.0.0.1:5000/api/employees?role=${role}&location=${location}&include_inactive=${includeInactive}`);
    const data = await res.json();
    const table = document.getElementById("empTable");
    table.innerHTML = "<tr><th>Name</th><th>Role</th><th>Location</th><th>Experience</th><th>Compensation</th><th>Status</th></tr>";
    data.forEach(e => {
        table.innerHTML += `<tr>
            <td>${e.name}</td><td>${e.role}</td><td>${e.location_name}</td>
            <td>${e.experience}</td><td>${e.compensation}</td><td>${e.status}</td>
        </tr>`;
    });
}

function downloadCSV() {
    const role = document.getElementById("role").value;
    const location = document.getElementById("location").value;
    const includeInactive = document.getElementById("inactive").checked;

    const params = new URLSearchParams({
        role: role,
        location: location,
        include_inactive: includeInactive
    });

    window.location.href = `http://127.0.0.1:5000/api/download-csv?${params.toString()}`;
}


async function simulateIncrement() {
    const percent = document.getElementById("incrementPercent").value;
    const res = await fetch("http://127.0.0.1:5000/api/simulate-increment", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ percent: percent })
    });
    const data = await res.json();
    const table = document.getElementById("simulatedTable");
    table.innerHTML = "<tr><th>Name</th><th>Current</th><th>Updated</th></tr>";
    data.forEach(e => {
        table.innerHTML += `<tr><td>${e.name}</td><td>${e.current_compensation}</td><td>${e.updated_compensation}</td></tr>`;
    });
}

async function loadExperienceDistribution() {
    const table = document.getElementById("experienceTable");
    table.querySelector("tbody").innerHTML = "<tr><td colspan='2'>Loading...</td></tr>";

    try {
        const res = await fetch("http://127.0.0.1:5000/api/experience-distribution");
        const data = await res.json();

        const tbody = table.querySelector("tbody");
        tbody.innerHTML = ""; // Clear old data

        data.forEach(row => {
            const tr = document.createElement("tr");
            tr.innerHTML = `<td>${row.experience_range}</td><td>${row.employee_count}</td>`;
            tbody.appendChild(tr);
        });

        // Optional: show a message if no data is returned
        if (data.length === 0) {
            tbody.innerHTML = "<tr><td colspan='2'>No data available</td></tr>";
        }

    } catch (error) {
        console.error("Error loading experience distribution:", error);
        const tbody = table.querySelector("tbody");
        tbody.innerHTML = "<tr><td colspan='2'>Error loading data</td></tr>";
    }
}

