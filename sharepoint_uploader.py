from shareplum import Site
from io import StringIO


class UploadToSharePoint:
    @staticmethod
    def upload(site_url, username, password, df):
        # create SharePoint site object
        # site_url = "https://worksite.sharepoint.com/sites/OG_49014"
        # username = "your-username"
        # password = "your-password"

        # create pandas dataframe
        # df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
        #                   'Age': [25, 30, 35]})

        # convert pandas dataframe to csv string
        csv_string = StringIO()
        df.to_csv(csv_string, index=False)

        # create file in Sharepoint
        sp_folder_url = "/your-sharepoint-folder-url/"
        sp_file_name = "example.csv"
        sp_site = Site(site_url, username, password)
        sp_folder = sp_site.Folder(sp_folder_url)
        sp_file = sp_folder.upload_file(csv_string.getvalue().encode(), sp_file_name)

        # print confirmation message
        print("File saved to Sharepoint!")
