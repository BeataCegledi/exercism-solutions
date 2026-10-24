/**
 * Log severity levels, each mapped to a numeric short code.
 */
public enum LogLevel {
    UNKNOWN(0),
    TRACE(1),
    DEBUG(2),
    INFO(4),
    WARNING(5),
    ERROR(6),
    FATAL(42);

    private final int shortLog;

    private LogLevel(int shortLog){
        this.shortLog = shortLog;
    }

    /** Returns the numeric short-format code for this level. */
    public int getShortLog(){
        return this.shortLog;
    }
}

