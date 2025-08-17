// Base URL from .env
const API_URL = import.meta.env.VITE_API_BASE_URL;

// --- Patients ---
export async function getPatients() {
  const response = await fetch(`${API_URL}/patients`);
  if (!response.ok) throw new Error('Failed to fetch patients');
  return response.json();
}

export async function getPatientById(id) {
  const response = await fetch(`${API_URL}/patients/${id}`);
  if (!response.ok) throw new Error(`Failed to fetch patient ${id}`);
  return response.json();
}

// --- Staff ---
export async function getStaff() {
  const response = await fetch(`${API_URL}/staff`);
  if (!response.ok) throw new Error('Failed to fetch staff');
  return response.json();
}

export async function getStaffById(id) {
  const response = await fetch(`${API_URL}/staff/${id}`);
  if (!response.ok) throw new Error(`Failed to fetch staff ${id}`);
  return response.json();
}

// --- Finance ---
export async function getFinanceRecords() {
  const response = await fetch(`${API_URL}/finance`);
  if (!response.ok) throw new Error('Failed to fetch finance records');
  return response.json();
}

export async function getFinanceById(id) {
  const response = await fetch(`${API_URL}/finance/${id}`);
  if (!response.ok) throw new Error(`Failed to fetch finance record ${id}`);
  return response.json();
}

// --- POST example (if needed) ---
export async function createPatient(patientData) {
  const response = await fetch(`${API_URL}/patients`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(patientData),
  });
  if (!response.ok) throw new Error('Failed to create patient');
  return response.json();
}
