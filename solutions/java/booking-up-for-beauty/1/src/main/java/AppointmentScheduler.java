import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

class AppointmentScheduler {
    public LocalDateTime schedule(String appointmentDateDescription) {
        DateTimeFormatter parser = DateTimeFormatter.ofPattern("MM/dd/yyyy HH:mm:ss");
        return LocalDateTime.parse(appointmentDateDescription, parser);        
    }

    public boolean hasPassed(LocalDateTime appointmentDate) {
        return appointmentDate.isBefore(LocalDateTime.now());
    }

    public boolean isAfternoonAppointment(LocalDateTime appointmentDate) {
        return (appointmentDate.getHour() >= 12 && appointmentDate.getHour() < 18);
    }

    public String getDescription(LocalDateTime appointmentDate) {
        DateTimeFormatter dateForm = DateTimeFormatter.ofPattern("EEEE, MMMM d, yyyy");
        DateTimeFormatter timeForm = DateTimeFormatter.ofPattern("h:mm a");
        return ("You have an appointment on " 
                + dateForm.format(appointmentDate) 
                + ", at " + timeForm.format(appointmentDate) + ".");
    }

    public LocalDate getAnniversaryDate() {
        return 	LocalDate.of(LocalDate.now().getYear(), 9, 15);
    }
}
