
# Represents a donation
# Normally this will be a database model somewhere.
class Donation:
    def __init__(self, donor, donation_type, quantity, date):
        self.donor = donor
        self.donation_type = donation_type
        self.quantity = quantity
        self.date = date
        self.status = 'Pending' # For now, can be 'Pending' or 'Complete'

# Abstracts a logging component
class DonationLogger:
    def __init__(self, log_filename='donations.log'):
        self.log_filename = log_filename

    # Logs the donation information.
    # Normally, a dedicated logging system will be used.
    def log_donation(self, donation):
        # For simplicity, just log the donation information to file for now
        with open(self.log_filename, "a") as log_file:
            log_file.write(f'{donation.donation_type} {donation.quantity} {donation.date}\n')

# Component to handle with reports creation
class Reports:
    def __init__(self):
        self.donation_stats = {}
        self.donor_stats = {}

    # Adds the donation information
    def add(self, donation):
        self.add_donation_info(donation)
        self.add_donor_info(donation)

    def add_donation_info(self, donation):
        if donation.donation_type not in self.donation_stats:
            self.donation_stats[donation.donation_type] = []
        self.donation_stats[donation.donation_type].append(donation)

    def add_donor_info(self, donation):
        if not donation.donor in self.donor_stats:
            self.donor_stats[donation.donor] = 0
        self.donor_stats[donation.donor] += donation.quantity

    # Creates a donations report.
    # For simplicity, just build and return a string containing donations information per type.
    def get_donations_report(self):
        report = 'Donations report:'

        for donation_type in self.donation_stats:
            report += f'\nDonation type {donation_type}:\n'
            for donation in self.donation_stats[donation_type]:
                report += f'Donor {donation.donor}, quantity {donation.quantity}, date {donation.date}, status {donation.status}\n'

        return report
    
    # Creates a donors report.
    # For simplicity, just build and return a string total amount donated per donor.
    def get_donors_report(self):
        report = 'Donors report:\n'
        
        for donor in self.donor_stats:
            report += f'Donor {donor}, total: {self.donor_stats[donor]}\n'

        return report

# A processor component, central to registering and handling donations.
class DonationProcessor:
    def __init__(self, log_filename='donations.log'):
        self.donation_logger = DonationLogger(log_filename) # composition
        self.reporter = Reports() # composition

    # Registers a donation (adds it to the system)
    # This will log the donation, and forward it to the reporter for stats recording.
    def register(self, donor, donation_type, quantity, date):
        # The problem statement mentions a donation status,
        # but does not specify any details.
        # For simplicity, mark a donation 'Pending' while it's processed, and 'Complete' afterwards

        donation = Donation(donor, donation_type, quantity, date)

        self.donation_logger.log_donation(donation)
        self.reports.add(donation)

        donation.status = 'Complete'

    # Wraps the reporter's get_donations_report
    def get_donations_report(self):
        return self.reporter.get_donations_report()

    # Wraps the reporter's get_donors_report
    def get_donors_report(self):
        return self.reporter.get_donors_report()

donation_processor = DonationProcessor()

donation_processor.register("Doina", "Food", 20, "03/22/24")
donation_processor.register("Doina", "Money", 30, "03/22/24")
donation_processor.register("Elena", "Clothing", 150, "04/2/24")
donation_processor.register("Kate", "Money", 250.50, "02/20/24")
donation_processor.register("Kate", "Clothing", 250.50, "02/20/24")

donations_report = donation_processor.get_donations_report()
print(donations_report)

donors_report = donation_processor.get_donors_report()
print(donors_report)
