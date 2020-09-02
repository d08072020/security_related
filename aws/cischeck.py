import sys
import configparser
import boto3

def v1_3_0_i3_1_Ensure_CloudTrail_is_enabled_in_all_regions(check=True):
    client = boto3.client('cloudtrail')
    if check:
        IsMultiRegionTrail = False
        IsLogging = False
        Target = None

        trails = client.describe_trails()
        for item in trails['trailList']:
            if item['IsMultiRegionTrail'] == True:
                Target = item
                IsMultiRegionTrail = True
                status = client.get_trail_status(Name=item['Name'])
                IsLogging = status['IsLogging']
                if IsLogging == True:
                    result = {'Passed':True,'IsMultiRegionTrail':IsMultiRegionTrail,'IsLogging':IsLogging,'Detail':Target}
                    return result
        result = {'Passed':False,'IsMultiRegionTrail':IsMultiRegionTrail,'IsLogging':IsLogging,'Detail':Target}
        return result
    else:
        pass

if __name__ == '__main__':
    if len(sys.argv)==3:
        config = configparser.ConfigParser()
        if sys.argv[1]=='check':
            outputfile=sys.argv[2]
            result = v1_3_0_i3_1_Ensure_CloudTrail_is_enabled_in_all_regions()
            config['3_1_Ensure_CloudTrail_is_enabled_in_all_regions'] = result
            print("3.1 Ensure CloudTrail is enabled in all regions,"+str(result['Passed']))

            with open(outputfile, 'w') as f:
                config.write(f)
    else:
        print('python cischeck.py check <config filename>')
