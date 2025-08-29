import scrapy

class DonorSpider(scrapy.Spider):
    name = "donors"
    start_urls = ["https://example.com/donors.html"]  # Replace with real/fake data source

    def parse(self, response):
        for donor in response.css("div.donor"):
            yield {
                "name": donor.css("span.name::text").get(),
                "blood_group": donor.css("span.blood::text").get(),
                "location": donor.css("span.location::text").get(),
                "contact": donor.css("span.contact::text").get(),
            }
