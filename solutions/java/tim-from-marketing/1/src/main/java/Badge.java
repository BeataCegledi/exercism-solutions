class Badge {
    public String print(Integer id, String name, String department) {
        String label;
        label = id == null ? name : ("[" + id + "] - " + name);
        label += department == null ? " - OWNER" : (" - " + department.toUpperCase());    
        return label;
    }
}
