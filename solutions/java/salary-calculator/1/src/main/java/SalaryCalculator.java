public class SalaryCalculator {
    public double salaryMultiplier(int daysSkipped) {
       if (daysSkipped >= 5) {return 0.85;}
            else {return 1.0;}                       
    }

    public int bonusMultiplier(int productsSold) {
       if (productsSold >= 20) {return 13;}
            else {return 10;}
    }

    public double bonusForProductsSold(int productsSold) {
        return (productsSold * bonusMultiplier(productsSold));
    }

    public double finalSalary(int daysSkipped, int productsSold) {
        double salary = (1000 * salaryMultiplier(daysSkipped) + bonusForProductsSold(productsSold));
        if (salary >= 2000) {return 2000;}
            else {return salary;}
    } 
}
