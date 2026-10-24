/**
 * Represents a single parsed log line in the format "[LVL]: message".
 */
public class LogLine {
    private final String logLine;

    public LogLine(String logLine) {
        this.logLine = logLine;
    }

    /**
     * Parses the log level from the line.
     * Returns {@code UNKNOWN} if the level is not recognized.
     */
    public LogLevel getLogLevel() {
        switch (logLine.substring(1,4)){
            case "INF": { return LogLevel.INFO; }
            case "DBG": { return LogLevel.DEBUG; }
            case "TRC": { return LogLevel.TRACE; }
            case "WRN": { return LogLevel.WARNING; }
            case "ERR": { return LogLevel.ERROR; }
            case "FTL": { return LogLevel.FATAL; } 
            default: {return LogLevel.UNKNOWN;}
       }
    }

    /**
     * Builds the short log format: "<code>:<message>".
     */
    public String getOutputForShortLog() {
        return getLogLevel().getShortLog()+ ":"+logLine.substring(7);
    }
}