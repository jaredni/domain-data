export async function fetchDomainData(domain_name: string, data_type: string) {
  const response = await fetch('http://localhost:8000/domain-data', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ domain_name, data_type }),
  });
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
}