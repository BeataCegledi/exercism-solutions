import java.time.LocalDate;
import java.time.LocalDateTime;

/**
 * Calculates the moment one gigasecond (10^9 seconds) after a given moment.
 */
public class Gigasecond {
    private static final long GIGASEC = 1_000_000_000;
    private final LocalDateTime moment;

    /**
     * @param moment the start date, interpreted as midnight (00:00:00)
     */
    public Gigasecond(LocalDate moment) {
        this.moment = moment.atStartOfDay();
    }

    /**
     * @param moment the start date and time
     */
    public Gigasecond(LocalDateTime moment) {
        this.moment = moment;
    }

    /**
     * @return the moment one gigasecond after the start
     */
    public LocalDateTime getDateTime() {
        return moment.plusSeconds(GIGASEC);
    }
}
