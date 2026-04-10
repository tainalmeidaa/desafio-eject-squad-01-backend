function initializeReservationModal() {
  const modal = document.querySelector("[data-reservation-modal]");
  const openButtons = document.querySelectorAll("[data-reservation-open]");
  const closeButtons = document.querySelectorAll("[data-reservation-close]");

  if (!modal) return;

  const form = modal.querySelector("[data-reservation-form]");
  const dateInput = modal.querySelector("[data-reservation-date]");
  const durationInputs = modal.querySelectorAll("[data-reservation-duration]");
  const startTimeSelect = modal.querySelector("[data-reservation-start-time]");
  const slotsUrl = form.dataset.slotsUrl;
  const csrfInput = form.querySelector("input[name=csrfmiddlewaretoken]");

  function getCookie(name) {
    const cookieValue = `; ${document.cookie}`;
    const parts = cookieValue.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(";").shift();
    return null;
  }

  function syncCsrfToken() {
    const csrfToken = getCookie("csrftoken");
    if (csrfToken && csrfInput) {
      csrfInput.value = csrfToken;
    }
  }

  function openModal() {
    modal.hidden = false;
    document.body.style.overflow = "hidden";
    dateInput.min = new Date().toISOString().split("T")[0];
    syncCsrfToken();
  }

  function closeModal() {
    modal.hidden = true;
    document.body.style.overflow = "";
  }

  openButtons.forEach((btn) => btn.addEventListener("click", openModal));
  closeButtons.forEach((btn) => btn.addEventListener("click", closeModal));

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !modal.hidden) closeModal();
  });

  function getSelectedDuration() {
    const checked = modal.querySelector("[data-reservation-duration]:checked");
    return checked ? checked.value : null;
  }

  function resetStartTime(message) {
    startTimeSelect.innerHTML = `<option value="">${message}</option>`;
    startTimeSelect.disabled = true;
  }

  async function loadAvailableSlots() {
    const date = dateInput.value;
    const duration = getSelectedDuration();

    if (!date || !duration) {
      resetStartTime("Escolha a data e a duração primeiro");
      return;
    }

    resetStartTime("Carregando horários...");

    try {
      const res = await fetch(`${slotsUrl}?date=${date}&duration=${duration}`);
      const data = await res.json();

      if (!res.ok) {
        resetStartTime(data.error || "Erro ao carregar horários.");
        return;
      }

      if (data.available_slots.length === 0) {
        resetStartTime("Nenhum horário disponível nesta data");
        return;
      }

      startTimeSelect.innerHTML =
        '<option value="">Selecione o horário</option>';
      for (const slot of data.available_slots) {
        const opt = document.createElement("option");
        opt.value = slot;
        opt.textContent = slot;
        startTimeSelect.appendChild(opt);
      }
      startTimeSelect.disabled = false;
    } catch {
      resetStartTime("Erro ao carregar horários");
    }
  }

  dateInput.addEventListener("change", loadAvailableSlots);
  durationInputs.forEach((input) =>
    input.addEventListener("change", loadAvailableSlots),
  );
  form.addEventListener("submit", syncCsrfToken);
}

initializeReservationModal();
