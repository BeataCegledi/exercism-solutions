
class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public static int[] getLastWeek() {
        int[] lastWeek = {0, 2, 5, 3, 7, 8, 4};
        return (lastWeek);
    }

    public int getToday() {
        return birdsPerDay[birdsPerDay.length - 1];
    }

    public void incrementTodaysCount() {
        birdsPerDay[birdsPerDay.length - 1]++;
    }

    public boolean hasDayWithoutBirds() {
        for (int count : birdsPerDay) {
        if (count == 0) return true;
        }
        return false;
    }

    public int getCountForFirstDays(int numberOfDays) {
        int sum = 0;
        if (numberOfDays > birdsPerDay.length) {numberOfDays = birdsPerDay.length;}
        for (int i = 0; i < numberOfDays; i++){
            sum += birdsPerDay[i];
        }
        return sum;
    }   

    public int getBusyDays() {
        int count = 0;
        for (int item : birdsPerDay){
           if (item >= 5) {
               count++;
           }
        }  
        return count;
    }
}
