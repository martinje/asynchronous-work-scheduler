# Submit a work request and capture the response
$response = Invoke-RestMethod -Method Post -Uri "http://localhost:5000/api"

# Extract the ID from the response
$id = $response.id

# Display the ID
Write-Host "Work request submitted with ID: $id"

# Check the status of the work request using the ID
$status_response = Invoke-RestMethod -Method Get -Uri ("http://localhost:5000/api?id=$id")

# Display the status response
Write-Host "Status of work request with ID $($id):"
$status_response
