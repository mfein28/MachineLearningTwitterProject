import pickle

import numpy
import pandas as pd
import csv
from sklearn.externals import joblib
from joblib import dump, load
import numpy as np
import tweepy
import csv
import emoji
from tweepy import OAuthHandler
import tkinter
from tkinter import *

ACities = ['Adjuntas', 'Aguada', 'Aguadilla', 'Anasco', 'Angeles', 'Arecibo', 'Aguas Buenas', 'Aguirre', 'Aibonito',
           'Arroyo', 'Agawam', 'Amherst', 'Adams', 'Ashley Falls', 'Ashfield',
           'Athol', 'Ashburnham', 'Ashby', 'Ayer', 'Auburn', 'Acton', 'Ashland', 'Andover', 'Amesbury', 'Accord',
           'Allston', 'Avon', 'Abington', 'Auburndale', 'Arlington', 'Arlington Heights',
           'Assonet', 'Attleboro', 'Acushnet', 'Attleboro Falls', 'Adamsville', 'Albion', 'Ashaway', 'Antrim',
           'Ashuelot', 'Acworth', 'Alstead', 'Alton', 'Alton Bay', 'Atkinson', 'Alfred', 'Augusta',
           'Abbot', 'Aurora', 'Alna', 'Addison', 'Anson', 'Athens', 'Ascutney', 'Alburgh', 'Adamant', 'Albany',
           'Averill', 'Amston', 'Ashford', 'Ansonia', 'Avenel', 'Allendale', 'Alpine', 'Adelphia', 'Allenhurst',
           'Asbury Park',
           'Atlantic Highlands', 'Avon By The Sea', 'Allamuchy', 'Alloway', 'Atco', 'Audubon', 'Absecon', 'Avalon',
           'Atlantic City', 'Allentown', 'Allenwood', 'Annandale', 'Asbury', 'Apo', 'Amawalk', 'Ardsley',
           'Ardsley On Hudson',
           'Armonk', 'Arden', 'Astoria', 'Albertson', 'Atlantic Beach', 'ABMPS', 'Arverne', 'Amityville', 'Amagansett',
           'Aquebogue', 'Alcove', 'Alplaus', 'Altamont', 'Amsterdam', 'Auriesville', 'Austerlitz', 'Averill Park',
           'Acra', 'Arkville', 'Amenia', 'Ancram', 'Ancramdale', 'Annandale On Hudson', 'Adirondack', 'Argyle',
           'Altona', 'Au Sable Forks', 'Apulia Station', 'Alder Creek', 'Altmar', 'Ava', 'Adams Center',
           'Alexandria Bay', 'Antwerp', 'Afton', 'Andes', 'Apalachin', 'Akron', 'Alden', 'Alexander', 'Angola',
           'Appleton', 'Arcade', 'Athol Springs', 'Attica', 'Adams Basin', 'Allegany', 'Alma', 'Angelica', 'Ashville',
           'Alfred Station', 'Almond', 'Arkport', 'Atlanta', 'Avoca', 'Aliquippa', 'Ambridge', 'Atlasburg',
           'Allison Park', 'Aleppo', 'Amity', 'Avella', 'Adah', 'Allenport', 'Allison', 'Acosta', 'Alum Bank', 'Acme',
           'Adamsburg', 'Alverton', 'Apollo', 'Ardara', 'Armbrust', 'Arona', 'Avonmore', 'Alverda', 'Anita', 'Arcadia',
           'Aultman', 'Armagh', 'Atlantic', 'Adrian', 'Altoona', 'Alexandria', 'Austin', 'Aaronsburg', 'Allport',
           'Alba', 'Arnot', 'Allensville', 'Annville', 'Amberson', 'Artemas', 'Abbottstown', 'Airville', 'Arendtsville',
           'Aspers', 'Antes Fort', 'Avis', 'Aristes', 'Ackermanville', 'Alburtis', 'Aquashicola', 'Albrightsville',
           'Andreas', 'Analomink', 'Archbald', 'Ambler', 'Ardmore', 'Aston', 'Atglen', 'Avondale', 'Arcola',
           'Adamstown', 'Aldie', 'Amissville', 'Ashburn', 'Abell', 'Accokeek', 'Aquasco', 'Avenue',
           'Annapolis Junction', 'Andrews Air Force Base', 'Ashton', 'Aberdeen', 'Aberdeen Proving Ground', 'APG',
           'Abingdon', 'Arnold', 'Annapolis', 'Accident', 'Allen', 'Aroda', 'Arrington', 'Achilles',
           'Amelia Court House', 'Ark', 'Arvonia', 'Aylett', 'Accomac', 'Assawoman', 'Alberta', 'Ammon', 'Ararat',
           'Axton', 'Appalachia', 'Atkins', 'Austinville', 'Augusta Springs', 'Altavista', 'Appomattox', 'Amonate',
           'Anawalt', 'Alderson', 'Arbovale', 'Alloy', 'Alum Creek', 'Amma', 'Arnett', 'Artie', 'Advent', 'Arnoldsburg',
           'Alkol', 'Apple Grove', 'Accoville', 'Amherstdale', 'Allen Junction', 'Amigo', 'Ansted', 'Alum Bridge',
           'Anmoore', 'Albright', 'Arthurdale', 'Advance', 'Alamance', 'Altamahaw', 'Asheboro', 'Angier', 'Apex',
           'Aulander', 'Ahoskie', 'Aydlett', 'Albemarle', 'Alexis', 'Ansonville', 'Autryville', 'Ash', 'Alliance',
           'Arapahoe', 'Ayden', 'Asheville', 'Andrews', 'Alcolu', 'Adams Run', 'Awendaw', 'Aynor', 'Abbeville',
           'Anderson', 'Aiken', 'Avondale Estates', 'Alpharetta', 'Adairsville', 'Aragon', 'Armuchee', 'Austell',
           'Ailey', 'Alamo', 'Alston', 'Alto', 'Arnoldsville', 'Appling', 'Avera', 'Ambrose', 'Adel', 'Alapaha',
           'Axson', 'Americus', 'Andersonville', 'Arabi', 'ABAC', 'Astor', 'Apalachicola', 'Alford', 'Altha', 'Alachua',
           'Anthony', 'Archer', 'Altamonte Springs', 'Apopka', 'Apollo Beach', 'Alturas', 'Avon Park', 'Alva',
           'Anna Maria', 'Aripeka', 'Astatula', 'Adger', 'Alabaster', 'Alexander City', 'Allgood', 'Arab', 'Abernant',
           'Aliceville', 'Arley', 'Albertville', 'Attalla', 'Autaugaville', 'Anniston', 'Ariton', 'Andalusia', 'Atmore',
           'Axis', 'Annemanie', 'Auburn University', 'Antioch', 'Ashland City', 'Auburntown', 'Apison', 'Arnold AFB',
           'Alcoa', 'Arthur', 'Atoka', 'Atwood', 'Allardt', 'Allons', 'Allred', 'Arkabutla', 'Alligator', 'Anguilla',
           'Algoma', 'Amory', 'Ackerman', 'Artesia', 'Attapulgus', 'Ages Brookside', 'Asher', 'Arjay', 'Artemus',
           'Argillite', 'Ashcamp', 'Auxier', 'Ary', 'Avawam', 'Almo', 'Adolphus', 'Alvaton', 'Adairville', 'Alpha',
           'Amlin', 'Ashley', 'Adelphi', 'Amanda', 'Alvordton', 'Archbold', 'Adena', 'Alledonia', 'Ashtabula',
           'Austinburg', 'Avon Lake', 'Atwater', 'Apple Creek', 'Alvada', 'Addyston', 'Amelia', 'AMF', 'Anna',
           'Arcanum', 'Amesville', 'Ada', 'Alger', 'Amo', 'Argos', 'Avilla', 'Amboy', 'Ambia', 'Algonac', 'Allenton',
           'Almont', 'Anchorville', 'Armada', 'Allen Park', 'Ann Arbor', 'Azalia', 'Auburn Hills', 'Applegate', 'Atlas',
           'Au Gres', 'Allegan', 'Alanson', 'Alpena', 'Allouez', 'Au Train', 'Ahmeek', 'Amasa', 'Atlantic Mine',
           'Ackworth', 'Adair', 'Alleman', 'Allerton', 'Ames', 'Ankeny', 'Albert City', 'Algona', 'Armstrong',
           'Ayrshire', 'Ackley', 'Alta Vista', 'Aplington', 'Aredale', 'Arispe', 'Alta', 'Anthon', 'Aurelia', 'Alvord',
           'Arnolds Park', 'Aspinwall', 'Arion', 'Andrew', 'Ainsworth', 'Alburnett', 'Amana', 'Anamosa', 'Agency',
           'Albia', 'Atalissa', 'Adell', 'Ashippun', 'Arena', 'Amery', 'Abrams', 'Amberg', 'Armstrong Creek',
           'Athelstane', 'Abbotsford', 'Amherst Junction', 'Aniwa', 'Antigo', 'Arpin', 'Argonne', 'Alma Center',
           'Arkdale', 'Arkansaw', 'Almena', 'Almelund', 'Anoka', 'Adolph', 'Alborn', 'Angora', 'Askov', 'Altura',
           'Albert Lea', 'Arco', 'Ah Gwah Ching', 'Aitkin', 'Akeley', 'Aldrich', 'Alvarado', 'Angle Inlet', 'Alcester',
           'Armour', 'Artesian', 'Akaska', 'Agar', 'Abercrombie', 'Absaraka', 'Argusville', 'Ayr', 'Aneta', 'Arvilla',
           'Agate', 'Alsen', 'Amidon', 'Anamoose', 'Antler', 'Arnegard', 'Absarokee', 'Antelope', 'Alzada', 'Angela',
           'Alder', 'Anaconda', 'Alberton', 'Arlee', 'Algonquin', 'Alsip', 'Aroma Park', 'Ashkum', 'Apple River',
           'Aledo', 'Annawan', 'Ancona', 'Anchor', 'Armington', 'Arrowsmith', 'Alvin', 'Ashmore', 'Alhambra',
           'Addieville', 'Albers', 'Aviston', 'Argenta', 'Assumption', 'Alsey', 'Arenzville', 'Alto Pass', 'Annada',
           'Anabel', 'Arbela', 'Altenburg', 'Arbyrd', 'Amazonia', 'Amoret', 'Appleton City', 'Archie', 'Auxvasse',
           'Arrow Rock', 'Ash Grove', 'Atchison', 'Axtell', 'Arma', 'Admire', 'Agenda', 'Andale', 'Argonia',
           'Arkansas City', 'Abilene', 'Assaria', 'Abbyville', 'Albert', 'Agra', 'Abie', 'Alvo', 'Alda', 'Anselmo',
           'Ansley', 'Ama', 'Abita Springs', 'Akers', 'Amite', 'Angie', 'Arnaudville', 'Avery Island', 'Addis',
           'Archibald', 'Aimwell', 'Anacoco', 'Alleene', 'Ashdown', 'Antoine', 'Arkadelphia', 'Adona', 'Almyra',
           'Altheimer', 'Amagon', 'Armorel', 'Aubrey', 'Alicia', 'Ash Flat', 'Alix', 'Altus', 'Alex', 'Amber',
           'Anadarko', 'Apache', 'Addington', 'Altus AFB', 'Arapaho', 'Aline', 'Amorita', 'Avant', 'Antlers', 'Achille',
           'Arkoma', 'Arthur City', 'Annona', 'Avery', 'Avinger', 'ARP', 'Apple Springs', 'Azle', 'Archer City',
           'Abbott', 'Aquilla', 'Art', 'Ace', 'Alief', 'Altair', 'Anahuac', 'Angleton', 'Austwell', 'Artesia Wells',
           'Atascosa', 'Adkins', 'Agua Dulce', 'Alice', 'Aransas Pass', 'Asherton', 'Alleyton', 'Alanreed', 'Amarillo',
           'Abernathy', 'Anton', 'Aspermont', 'Ackerly', 'Arvada', 'Allenspark', 'Ault', 'Arriba', 'Aguilar', 'Alamosa',
           'Antonito', 'Arboles', 'Aspen', 'Albin', 'Alcova', 'Arminto', 'Aladdin', 'American Falls', 'Arbon', 'Arimo',
           'Atomic City', 'Ahsahka', 'Altonah', 'American Fork', 'Aneth', 'Annabella', 'Antimony', 'Apache Junction',
           'Arizona City', 'ASU', 'Aguila', 'Ajo', 'Arivaca', 'Amado', 'Ash Fork', 'Algodones', 'Albuquerque', 'Aztec',
           'Abiquiu', 'Alcalde', 'Amalia', 'Arroyo Hondo', 'Arroyo Seco', 'Angel Fire', 'Anton Chico', 'Arrey',
           'Animas', 'Arenas Valley', 'Alamogordo', 'Amistad', 'Amargosa Valley', 'AARP', 'Altadena', 'Agoura Hills',
           'Azusa', 'Adelanto', 'Angelus Oaks', 'Apple Valley', 'Aguanga', 'Anza', 'Aliso Viejo', 'Anaheim', 'Alpaugh',
           'Armona', 'Arvin', 'Avenal', 'Arroyo Grande', 'Atascadero', 'Avila Beach', 'Ahwahnee', 'Auberry', 'Atherton',
           'Alameda', 'American Canyon', 'Angwin', 'Aptos', 'Alviso', 'Aromas', 'Acampo', 'Altaville', 'Angels Camp',
           'Alderpoint', 'Arcata', 'Amador City', 'Alleghany', 'Arbuckle', 'Artois', 'Adin', 'Aiea', 'Anahola',
           'Agana Heights', 'Agat', 'Arch Cape', 'Alsea', 'Aumsville', 'Agness', 'Alvadore', 'Azalea', 'Ashwood',
           'Athena', 'Arock', 'Anacortes', 'Anderson Island', 'Adna', 'Allyn', 'Amanda Park', 'Ariel', 'Ardenvoir',
           'Airway Heights', 'Addy', 'Almira', 'Anatone', 'Asotin', 'Anchorage', 'Adak', 'Atka', 'Akiachak', 'Akiak',
           'Akutan', 'Alakanuk',
           'Aleknagik', 'Anchor Point', 'Aniak', 'Anvik', 'Allakaket', 'Anaktuvuk Pass', 'Arctic Village', 'Atqasuk',
           'Angoon', 'Auke Bay']
BCities = ['Bajadero', 'Barceloneta', 'Boqueron', 'Barranquitas', 'Bayamon', 'Barre', 'Belchertown', 'Blandford',
           'Bondsville',
           'Brimfield', 'Becket', 'Berkshire', 'Bernardston', 'Buckland', 'Baldwinville', 'Berlin', 'Blackstone',
           'Boylston', 'Brookfield',
           'Boxborough', 'Bedford', 'Bolton', 'Burlington', 'Billerica', 'Beverly', 'Boxford', 'Byfield', 'Bellingham',
           'Brant Rock', 'Boston',
           'Brighton', 'Braintree', 'Brockton', 'Bridgewater', 'Bryantville', 'Brookline', 'Brookline Village',
           'Babson Park', 'Belmont', 'Buzzards Bay',
           'Barnstable', 'Brewster', 'Berkley', 'Barrington', 'Block Island', 'Bradford', 'Bristol', 'Barnstead', 'Bow',
           'Bennington', 'Bethlehem', 'Bretton Woods',
           'Bath', 'Bartlett', 'Berwick', 'Bailey Island', 'Bar Mills', 'Biddeford', 'Biddeford Pool', 'Bowdoinham',
           'Bridgton', 'Brownfield', 'Brunswick', 'Bustins Island',
           'Buxton', 'Bethel', 'Bryant Pond', 'Buckfield', 'Bowdoin', 'Bangor', 'Bradley', 'Brewer', 'Brookton',
           'Brownville', 'Brownville Junction', 'Bucksport', 'Boothbay',
           'Boothbay Harbor', 'Bremen', 'Bar Harbor', 'Beals', 'Bernard', 'Birch Harbor', 'Blue Hill', 'Brooklin',
           'Brooksville', 'Bass Harbor', 'Baileyville', 'Benedicta',
           'Blaine', 'Belfast', 'Belgrade', 'Belgrade Lakes', 'Bingham', 'Brooks', 'Burnham', 'Barnard',
           'Bridgewater Corners', 'Brownsville', 'Bellows Falls', 'Brattleboro',
           'Bondville', 'BTV', 'Bakersfield', 'Belvidere Center', 'Benson', 'Bomoseen', 'Brandon', 'Bridport', 'Barnet',
           'Barton', 'Beebe Plain', 'Beecher Falls', 'Bloomfield',
           'Broad Brook', 'Barkhamsted', 'Ballouville', 'Brooklyn', 'Baltic', 'Bozrah', 'Beacon Falls', 'Botsford',
           'Branford', 'Bethany', 'Bridgeport', 'Bantam', 'Bayonne',
           'Boonton', 'Belleville', 'Bloomingdale', 'Butler', 'Bogota', 'Bergenfield', 'Belmar', 'Belford',
           'Bradley Beach', 'Belvidere', 'Blairstown', 'Branchville', 'Budd Lake',
           'Buttzville', 'Basking Ridge', 'Bedminster', 'Berkeley Heights', 'Bernardsville', 'Brookside', 'Barnegat',
           'Barnegat Light', 'Beach Haven', 'Birmingham', 'Blackwood',
           'Browns Mills', 'Bellmawr', 'Brigantine', 'Bridgeton', 'Buena', 'Belle Mead', 'Blawenburg', 'Bordentown',
           'Bayville', 'Beachwood', 'Brick', 'Brielle', 'Baptistown',
           'Bloomsbury', 'Bound Brook', 'Broadway', 'Bronx', 'Baldwin Place', 'Bedford Hills', 'Briarcliff Manor',
           'Buchanan', 'Bronxville', 'Bear Mountain', 'Bellvale', 'Blauvelt',
           'Blooming Grove', 'Bullville', 'Bellerose Village', 'Bayside', 'Bellerose', 'Baldwin', 'Breezy Point',
           'Babylon', 'Bayport', 'Bay Shore', 'Bellmore', 'Bellport', 'Bethpage',
           'Blue Point', 'Bohemia', 'Brentwood', 'Brightwaters', 'Brookhaven', 'Bridgehampton', 'Ballston Lake',
           'Ballston Spa', 'Berne', 'Brainard', 'Broadalbin', 'Burnt Hills',
           'Buskirk', 'Bearsville', 'Big Indian', 'Bloomington', 'Boiceville', 'Bangall', 'Barrytown', 'Beacon',
           'Billings', 'Barryville', 'Bloomingburg', 'Burlingham', 'Bakers Mills', 'Blue Mountain Lake',
           'Bolton Landing', 'Brant Lake', 'Bombay', 'Brainardsville', 'Brushton', 'Burke', 'Baldwinsville',
           'Bernhards Bay', 'Brewerton', 'Barneveld', 'Beaver Falls', 'Blossvale',
           'Boonville', 'Bouckville', 'Brantingham', 'Burlington Flats', 'Black River', 'Brasher Falls', 'Brier Hill',
           'Bainbridge', 'Bible School Park', 'Blodgett Mills',
           'Bloomville', 'Bovina Center', 'Binghamton', 'Barker', 'Basom', 'Batavia', 'Bliss', 'Bowmansville', 'Brant',
           'Burt', 'Buffalo', 'Bellona', 'Bergen', 'Branchport',
           'Brockport', 'Byron', 'Bemus Point', 'Black Creek', 'Bolivar', 'Brocton', 'Beaver Dams', 'Big Flats',
           'Breesport', 'Brooktondale', 'Burdett', 'Baden', 'Bairdford',
           'Bakerstown', 'Beaver', 'Belle Vernon', 'Brackenridge', 'Bradfordwoods', 'Bridgeville', 'Buena Vista',
           'Bulger', 'Bunola', 'Burgettstown', 'Bethel Park', 'Braddock',
           'Beallsville', 'Bentleyville', 'Bobtown', 'Brave', 'Boswell', 'Boynton', 'Breezewood', 'Buffalo Mills',
           'Bovard', 'Bradenville', 'Big Run', 'Black Lick', 'Blairsville',
           'Brush Valley', 'Burnside', 'Benezett', 'Brandy Camp', 'Brockway', 'Brookville', 'Byrnedale', 'Beaverdale',
           'Belsano', 'Boyers', 'Branchton', 'Bruin', 'Bessemer', 'Beyer',
           'Bear Lake', 'Beccaria', 'Bellwood', 'Blandburg', 'Brisbin', 'Broad Top', 'Beech Creek', 'Bellefonte',
           'Bigler', 'Blanchard', 'Boalsburg', 'Blossburg', 'Berrysburg', 'Blain',
           'Boiling Springs', 'Big Cove Tannery', 'Blairs Mills', 'Blue Ridge Summit', 'Burnt Cabins', 'Bendersville',
           'Biglerville', 'Brogue', 'Bart', 'Bausman', 'Bird In Hand', 'Blue Ball',
           'Brownstown', 'Beaver Springs', 'Beavertown', 'Benton', 'Bloomsburg', 'Branchdale', 'Bowmanstown',
           'Breinigsville', 'Barnesville', 'Beaver Meadows', 'Bartonsville', 'Brodheadsville',
           'Buck Hill Falls', 'Bushkill', 'Beach Lake', 'Bear Creek', 'Blakeslee', 'Brackney', 'Blooming Glen',
           'Buckingham', 'Bala Cynwyd', 'Broomall', 'Bryn Athyn', 'Bryn Mawr', 'Bensalem', 'Berwyn',
           'Brandamore', 'Birchrunville', 'Blue Bell', 'Bally', 'Barto', 'Bechtelsville', 'Bernville', 'Birdsboro',
           'Blandon', 'Bowers', 'Boyertown', 'Bear', 'Bethany Beach', 'Bluemont', 'Bristow', 'Broad Run',
           'Barstow', 'Bel Alton', 'Benedict', 'Brandywine', 'Broomes Island', 'Bryans Road', 'Bryantown', 'Bushwood',
           'Beltsville', 'Bladensburg', 'Bowie', 'Bethesda', 'Brookeville', 'Boyds', 'Brinklow', 'Burtonsville',
           'Bel Air', 'Belcamp', 'Boring', 'Brooklandville', 'Baltimore', 'Bittinger', 'Barclay', 'Betterton', 'Bozman',
           'Big Pool', 'Boonsboro', 'Braddock Heights', 'Buckeystown', 'Burkittsville', 'Bishopville', 'Bivalve',
           'Bowling Green', 'Brooke', 'Burgess', 'Burr Hill', 'Bentonville', 'Berryville', 'Boyce', 'Brucetown',
           'Banco', 'Bealeton', 'Brandy Station', 'Brightwood', 'Basye', 'Bergton', 'Barboursville', 'Batesville',
           'Barhamsville',
           'Beaumont', 'Beaverdam', 'Bena', 'Bohannon', 'Bremo Bluff', 'Bruington', 'Bumpass', 'Battery Park',
           'Belle Haven', 'Birdsnest', 'Bloxom', 'Boykins', 'Baskerville', 'Boydton', 'Bracey', 'Brodnax', 'Burkeville',
           'Bassett', 'Belspring',
           'Bent Mountain', 'Blacksburg', 'Blue Ridge', 'Boones Mill', 'Bee', 'Ben Hur', 'Big Stone Gap', 'Birchleaf',
           'Blackwater', 'Barren Springs', 'Bastian', 'Bland', 'Broadford', 'Bacova', 'Blue Grass', 'Brownsburg',
           'Big Island',
           'Blairs', 'Brookneal', 'Buffalo Junction', 'Bandy', 'Big Rock', 'Bishop', 'Bluefield', 'Boissevain',
           'Breaks', 'Burkes Garden', 'Beeson', 'Bramwell', 'Bud', 'Bartley', 'Berwind', 'Big Sandy', 'Bradshaw',
           'Brenton', 'Ballard',
           'Bartow', 'Buckeye', 'Bancroft', 'Belle', 'Bickmore', 'Bim', 'Blair', 'Bloomingrose', 'Blount', 'Blue Creek',
           'Bob White', 'Bomont', 'Boomer', 'Bakerton', 'Berkeley Springs', 'Bunker Hill', 'Big Creek', 'Branchland',
           'Baisden',
           'Bruno', 'Borderland', 'Breeden', 'Beckley', 'Bolt', 'Beech Bottom', 'Benwood', 'Big Bend', 'Big Springs',
           'Brohard', 'Buckhannon', 'Belington', 'Bowden', 'Bergoo', 'Berea', 'Burnsville', 'Blacksville', 'Bretz',
           'Bruceton Mills',
           'Barrackville', 'Baxter', 'Burton', 'Birch River', 'Belva', 'Bayard', 'Baker', 'Bloomery', 'Belews Creek',
           'Bethania', 'Bennett', 'Biscoe', 'Blanch', 'Bonlee', 'Browns Summit', 'Bynum', 'Bahama', 'Buies Creek',
           'Bullock', 'Bunn', 'Butner', 'Bailey', 'Battleboro',
           'Belhaven', 'Bellarthur', 'Blounts Creek', 'Barco', 'Badin', 'Barium Springs', 'Bessemer City', 'Bostic',
           'Bladenboro', 'Bunnlevel', 'Bolivia', 'Burgaw', 'Bayboro', 'Beaufort', 'Beulaville', 'Banner Elk',
           'Blowing Rock', 'Boone', 'Bakersville', 'Balsam',
           'Balsam Grove', 'Barnardsville', 'Bat Cave', 'Black Mountain', 'Brevard', 'Bryson City', 'Brasstown',
           'Ballentine', 'Bamberg', 'Batesburg', 'Bethune', 'Blackstock', 'Blythewood', 'Bowman', 'Bethera', 'Bonneau',
           'Bennettsville', 'Blenheim', 'Belton', 'Barnwell',
           'Blackville', 'Beech Island', 'Bluffton', 'Brunson', 'Ball Ground', 'Bowdon', 'Bowdon Junction', 'Bellville',
           'Brooklet', 'Buford', 'Bowersville', 'Braselton', 'Bogart', 'Bostwick', 'Buckhead', 'Blythe', 'Boneville',
           'Bolingbroke', 'Bonaire', 'Byromville',
           'Baxley', 'Blackshear', 'Broxton', 'Barney', 'Baconton', 'Barwick', 'Box Springs', 'Bryceville',
           'Barberville', 'Bunnell', 'Bascom', 'Blountstown', 'Bonifay', 'Bagdad', 'Bell', 'Bronson', 'Brooker',
           'Big Pine Key', 'Boynton Beach', 'Boca Raton', 'Belle Glade',
           'Balm', 'Bushnell', 'Bay Pines', 'Belleair Beach', 'Boca Grande', 'Bokeelia', 'Bonita Springs', 'Bradenton',
           'Bradenton Beach', 'Belleview', 'Beverly Hills', 'BVL', 'Baileyton', 'Blountsville', 'Bon Air', 'Brent',
           'Brierfield', 'Burnwell', 'Boligee', 'Brookwood',
           'Buhl', 'Bankston', 'Beaverton', 'Belk', 'Berry', 'Brilliant', 'Belle Mina', 'Brownsboro', 'Boaz', 'Bryant',
           'Banks', 'Billingsley', 'Booth', 'Brantley', 'Brundidge', 'Black', 'Beatrice', 'Brewton', 'Bay Minette',
           'Bayou La Batre', 'Bon Secour', 'Bucks', 'Boykin',
           'Bellamy', 'Beechgrove', 'Bell Buckle', 'Bon Aqua', 'Bradyville', 'Bumpus Mills', 'Burns', 'Bakewell',
           'Beersheba Springs', 'Birchwood', 'Blountville', 'Bluff City', 'Bean Station', 'Briceville', 'Bulls Gap',
           'Bybee', 'Bells', 'Braden', 'Burlison', 'Bath Springs',
           'Beech Bluff', 'Bethel Springs', 'Bruceton', 'Bloomington Springs', 'Brush Creek', 'Buffalo Valley',
           'Byrdstown', 'Belen', 'Blue Mountain', 'Byhalia', 'Benoit', 'Beulah', 'Boyle', 'Baldwyn', 'Becker', 'Belden',
           'Blue Springs', 'Booneville', 'Banner', 'Bruce', 'Belzoni',
           'Bentonia', 'Braxton', 'Byram', 'Buckatunna', 'Bassfield', 'Bay Springs', 'Bay Saint Louis', 'Biloxi',
           'Bogue Chitto', 'Bude', 'Bellefontaine', 'Blakely', 'Brinson', 'Bronwood', 'Bardstown', 'Bradfordsville',
           'Buckner', 'Battletown', 'Brandenburg', 'Burgin', 'Bighill',
           'Brodhead', 'Bryantsville', 'Bush', 'Benham', 'Big Laurel', 'Bledsoe', 'Barbourville', 'Bimble',
           'Bryants Store', 'Bellevue', 'Beauty', 'Boons Camp', 'Bays', 'Beattyville', 'Belcher', 'Belfry', 'Burdine',
           'Betsy Layne', 'Bevinsville', 'Blue River', 'Bypro', 'Bear Branch',
           'Bonnyman', 'Buckhorn', 'Bulan', 'Busy', 'Blackey', 'Bandana', 'Bardwell', 'Barlow', 'Burna', 'Bee Spring',
           'Beaver Dam', 'Beech Grove', 'Beechmont', 'Browder', 'Baskett', 'Bethelridge', 'Bronston', 'Big Clifty',
           'Bonnieville', 'Breeding', 'Burkesville', 'Blacklick', 'Brinkhaven',
           'Buckeye Lake', 'Brice', 'Belle Center', 'Bradner', 'Burgoon', 'Berkey', 'Bryan', 'Belle Valley',
           'Blue Rock', 'Byesville', 'Blissfield', 'Bellaire', 'Bergholz', 'Bannock', 'Bay Village', 'Brecksville',
           'Brookpark', 'Broadview Heights', 'Barberton', 'Brady Lake', 'Burbank', 'Berlin Center',
           'Bristolville', 'Burghill', 'Beach City', 'Beloit', 'Big Prairie', 'Bowerston', 'Berlin Heights',
           'Bettsville', 'Bloomdale', 'Bucyrus', 'Blanchester', 'Bellbrook', 'Botkins', 'Burkettsville', 'Bidwell',
           'Bourneville', 'Belpre', 'Buchtel', 'Belmore', 'Benton Ridge', 'Bargersville', 'Boggstown',
           'B M G', 'Beverly Shores', 'Boone Grove', 'Bourbon', 'Burket', 'Bippus', 'Bringhurst', 'Burrows', 'Borden',
           'Butlerville', 'Bicknell', 'Birdseye', 'Bruceville', 'Buckskin', 'Blanford', 'Brazil', 'Battle Ground',
           'Brook', 'Brookston', 'Buck Creek', 'Burnettsville', 'Bloomfield Hills', 'Bad Axe',
           'Birch Run', 'Brown City', 'Bentley', 'Breckenridge', 'Barton City', 'Bay City', 'Bay Port', 'Bannister',
           'Belding', 'Battle Creek', 'Benton Harbor', 'Breedsville', 'Burr Oak', 'Baroda', 'Berrien Center',
           'Berrien Springs', 'Bridgman', 'Britton', 'Barryton', 'Big Rapids', 'Bitely', 'Brohman',
           'Burnips', 'Byron Center', 'Branch', 'Benzonia', 'Boon', 'Brethren', 'Buckley', 'Barbeau', 'Boyne City',
           'Boyne Falls', 'Brimley', 'Brutus', 'Burt Lake', 'Beaver Island', 'Bark River', 'Big Bay', 'Baraga',
           'Bergland', 'Bruce Crossing', 'Bagley', 'Barnes City', 'Bevington', 'Blairsburg', 'Bondurant',
           'Bouton', 'Boxholm', 'Brayton', 'Bussey', 'Belmond', 'Britt', 'Buffalo Center', 'Badger', 'Barnum', 'Bode',
           'Bradgate', 'Beaman', 'Blockton', 'Brunsville', 'Boyden', 'Breda', 'Blencoe', 'Braddyville', 'Belle Plaine',
           'Blakesburg', 'Bonaparte', 'Bettendorf', 'Belgium', 'Benet Lake', 'Black Earth', 'Blanchardville',
           'Blue Mounds', 'Browntown', 'Beetown', 'Boscobel', 'Baraboo', 'Briggsville', 'Burnett', 'Beldenville',
           'Bonduel', 'Brillion', 'Baileys Harbor', 'Brussels', 'Babcock', 'Birnamwood', 'Blenker', 'Bowler', 'Brokaw',
           'Boulder Junction', 'Brantwood', 'Butternut', 'Black River Falls', 'Bloomer', 'Boyceville', 'Boyd',
           'Balsam Lake', 'Barron', 'Barronett', 'Bayfield', 'Brill', 'Brule', 'Big Falls', 'Butte Des Morts', 'Braham',
           'Brook Park', 'Big Lake', 'Bird Island', 'Brownton', 'Buffalo Lake', 'Beaver Bay', 'Brimson', 'Babbitt',
           'Biwabik', 'Bovey', 'Blooming Prairie', 'Brownsdale', 'Blue Earth', 'Bricelyn', 'Balaton', 'Beaver Creek',
           'Bigelow', 'Bingham Lake', 'Butterfield', 'Barry', 'Beardsley', 'Belview', 'Blomkest', 'Browns Valley',
           'Barrett', 'Bock', 'Bowlus', 'Brooten', 'Buckman', 'Burtrum', 'Brainerd', 'Backus', 'Bertha', 'Browerville',
           'Battle Lake', 'Bejou', 'Beltrami', 'Borup', 'Bemidji', 'Baudette', 'Bigfork', 'Birchdale', 'Blackduck',
           'Bowstring', 'Beresford', 'Brookings', 'Big Stone City', 'Brandt', 'Bonesteel', 'Bowdle', 'Brentford',
           'Blunt', 'Bison', 'Bullhead', 'Batesland', 'Belle Fourche', 'Black Hawk', 'Box Elder', 'Buffalo Gap',
           'Bathgate', 'Balta', 'Belcourt', 'Bisbee', 'Bottineau', 'Brocket', 'Binford', 'Bismarck', 'Beach',
           'Belfield', 'Balfour', 'Bantry', 'Berthold', 'Bowbells', 'Butte', 'Ballantine', 'Bearcreek', 'Bighorn',
           'Big Timber', 'Birney', 'Bridger', 'Broadview', 'Busby', 'Bainville', 'Biddle', 'Boyes', 'Broadus',
           'Brusett', 'Babb', 'Belt', 'Black Eagle', 'Brady', 'Browning', 'Basin', 'Boulder', 'Bozeman', 'Big Sky',
           'Bonner', 'Big Arm', 'Buffalo Grove', 'Bensenville', 'Berkeley', 'Beecher', 'Blue Island', 'Braceville',
           'Braidwood', 'Bolingbrook', 'Bridgeview', 'Bedford Park', 'Beaverville', 'Bonfield', 'Bourbonnais',
           'Buffalo Prairie', 'Buda', 'Bureau', 'Bardolph', 'Biggsville', 'Bishop Hill', 'Blandinsville', 'Bellflower',
           'Bement', 'Broadlands', 'Batchtown', 'Benld', 'Bethalto', 'Bartelso', 'Beckemeyer', 'Breese', 'Basco',
           'Baylis', 'Bowen', 'Beecher City', 'Beason', 'Blue Mound', 'Boody', 'Bulpitt', 'Beardstown', 'Bluffs',
           'Bluff Springs', 'Barnhill', 'Belle Rive', 'Bellmont', 'Bluford', 'Bone Gap', 'Bonnie', 'Broughton',
           'Browns', 'Burnt Prairie', 'Belknap', 'Boles', 'Brookport', 'Buncombe', 'Ballwin', 'Barnhart', 'Berger',
           'Baring', 'Bevier', 'Brashear', 'Blackwell', 'Bloomsdale', 'Bonne Terre', 'Bunker', 'Bell City', 'Brazeau',
           'Brownwood', 'Burfordville', 'Bernie', 'Bertrand', 'Blodgett', 'Braggadocio', 'Bragg City', 'Briar',
           'Broseley', 'Bates City', 'Blythedale', 'Bolckow', 'Burlington Junction', 'Bogard', 'Bosworth', 'Braymer',
           'Bucklin', 'Bronaugh', 'Barnett', 'Bonnots Mill', 'Brumley', 'Benton City', 'Bunceton', 'Blackburn',
           'Birch Tree', 'Bixby', 'Boss', 'Brinktown', 'Blue Eye', 'Bois D Arc', 'Bradleyville', 'Branson', 'Brixey',
           'Bruner', 'Brandsville', 'Baldwin City', 'Basehor', 'Bendena', 'Bonner Springs', 'Beattie', 'Belvue', 'Bern',
           'Berryton', 'Blue Rapids', 'Burlingame', 'Baxter Springs', 'Burdick', 'Barnes', 'Burden', 'Burrton', 'Byers',
           'Bushton', 'Bazine', 'Beeler', 'Brownell', 'Buhler', 'Bogue', 'Bird City', 'Boys Town', 'Barneston',
           'Beaver Crossing', 'Bennet', 'Brock', 'Bruning', 'Burchard', 'Burr', 'Beemer', 'Boelus', 'Broken Bow',
           'Burwell', 'Beaver City', 'Bladen', 'Benkelman', 'Broadwater', 'Barataria', 'Belle Chasse', 'Boothville',
           'Boutte', 'Braithwaite', 'Buras', 'Belle Rose', 'Bourg', 'Bogalusa', 'Basile', 'Breaux Bridge', 'Broussard',
           'Batchelor', 'Brittany', 'Brusly', 'Baton Rouge', 'Bienville', 'Barksdale AFB', 'Bossier City', 'Baskin',
           'Bastrop', 'Bernice', 'Bonita', 'Bordelonville', 'Bunkie', 'Ball', 'Bearden', 'Beirne', 'Ben Lomond',
           'Blevins', 'Board Camp', 'Bonnerdale', 'Bald Knob', 'Bauxite', 'Beebe', 'Bee Branch', 'Beedeville',
           'Brinkley', 'Blytheville', 'Brickeys', 'Burdette', 'Bay', 'Biggers', 'Black Oak', 'Black Rock', 'Bono',
           'Brookland', 'Bexar', 'Brockwell', 'Bergman', 'Big Flat', 'Bull Shoals', 'Bella Vista', 'Barling', 'Binger',
           'Burneyville', 'Bessie', 'Burns Flat', 'Balko', 'Boise City', 'Barnsdall', 'Bartlesville', 'Broken Arrow',
           'Big Cabin', 'Bluejacket', 'Beggs', 'Braggs', 'Blanco', 'Blocker', 'Bromide', 'Braman', 'Battiest',
           'Bokchito', 'BB', 'Boley', 'Bowlegs', 'Byars', 'Bokoshe', 'Bunch', 'Balch Springs', 'Bagwell',
           'Ben Franklin', 'Blossom', 'Bogata', 'Bonham', 'Bivins', 'Bloomburg', 'Beckville', 'Ben Wheeler', 'Bullard',
           'Bon Wier', 'Broaddus', 'Brookeland', 'Burleson', 'Bluegrove', 'Burkburnett', 'Bryson', 'Blanket',
           'Bluff Dale', 'Buckholts', 'Blum', 'Bremond', 'Ballinger', 'Bangs', 'Bend', 'Brookesmith', 'Burkett',
           'Bronte', 'Beasley', 'Blessing', 'Boling', 'Brazoria', 'Brookshire', 'Bacliff', 'Batson', 'Baytown',
           'Bridge City', 'Buna', 'Bedias', 'Brenham', 'Bandera', 'Bergheim', 'Bigfoot', 'Boerne', 'Beeville',
           'Berclair', 'Bulverde', 'Banquete', 'Benavides', 'Ben Bolt', 'Bruni', 'Bertram', 'Briggs', 'Buchanan Dam',
           'Burnet', 'Barksdale', 'Big Wells', 'Brackettville', 'Bleiblerville', 'Booker', 'Borger', 'Bovina',
           'Boys Ranch', 'Briscoe', 'Bushland', 'Baird', 'Benjamin', 'Balmorhea', 'Big Spring',
           'Big Bend National Park', 'Broomfield', 'Bond', 'Buffalo Creek', 'Bellvue', 'Berthoud', 'Briggsdale',
           'Brush', 'Boncarbo', 'Blanca', 'Bedrock', 'Basalt', 'Battlement Mesa', 'Bosler', 'Baggs', 'Bairoil',
           'Big Horn', 'Big Piney', 'Blackfoot', 'Burley', 'Bruneau', 'Boise', 'Bayview', 'Bonners Ferry', 'Bovill',
           'Bingham Canyon', 'Bluebell', 'Bonanza', 'Bountiful', 'Bear River City', 'Brigham City', 'Blanding', 'Bluff',
           'Beryl', 'Brian Head', 'Bryce', 'Bapchule', 'Black Canyon City', 'Bouse', 'Bylas', 'Blue', 'Bellemont',
           'Bullhead City', 'Blue Gap', 'Bernalillo', 'Bluewater', 'Bosque', 'Bosque Farms', 'Brimhall', 'Berino',
           'Bent', 'Bard', 'Beatty', 'Blue Diamond', 'Boulder City', 'Bunkerville', 'Battle Mountain', 'Bell Gardens',
           'Buena Park',
           'Baldwin Park', 'Boulevard', 'Bonsall', 'Borrego Springs', 'Banning', 'Brawley', 'Big Bear City',
           'Big Bear Lake', 'Blue Jay', 'Brea', 'Brandeis', 'Bodfish', 'Buttonwillow', 'Buellton', 'Big Pine', 'Boron',
           'Bass Lake', 'Biola', 'Burrel', 'Big Sur', 'Brisbane', 'Benicia', 'Bethel Island', 'Birds Landing',
           'Belvedere Tiburon', 'Bodega', 'Bodega Bay', 'Bolinas', 'Boulder Creek', 'Brookdale', 'Burson', 'Ballico',
           'Big Oak Flat', 'Boyes Hot Springs', 'Branscomb', 'Blocksburg', 'Blue Lake', 'Burnt Ranch', 'Beale AFB',
           'Berry Creek', 'Biggs', 'Butte City', 'Bieber', 'Big Bar', 'Burney', 'Blairsden-Graeagle', 'Beckwourth',
           'Barrigada', 'Beavercreek', 'Bridal Veil', 'Bandon', 'Blachly', 'Broadbent', 'Butte Falls', 'Bly',
           'Brothers', 'Baker City', 'Bates', 'Boardman', 'Brogan', 'Black Diamond', 'Bothell', 'Bainbridge Island',
           'Blakely Island', 'Bremerton', 'Brinnon', 'Bonney Lake', 'Bay Center', 'Belfair',
           'Bucoda', 'Bingen', 'Brush Prairie', 'Benge', 'Bickleton', 'Barrow', 'Bettles Field', 'Brevig Mission']
CCities = ['Cabo Rojo', 'Camuy', 'Castaner', 'Ciales', 'Caguas', 'Canovanas', 'Ceiba',
           'Cayey', 'Cidra', 'Coamo', 'Culebra', 'Coto Laurel', 'Comerio', 'Corozal', 'Christiansted',
           'Catano', 'Carolina', 'Chester', 'Chesterfield', 'Chicopee', 'Cummington', 'Cheshire', 'Charlemont',
           'Colrain', 'Conway', 'Charlton', 'Charlton City', 'Charlton Depot', 'Clinton', 'Cherry Valley', 'Carlisle',
           'Concord',
           'Chelmsford', 'Canton', 'Cohasset', 'Charlestown', 'Cambridge', 'Chelsea', 'Carver', 'Chestnut Hill',
           'Cataumet', 'Chilmark', 'Centerville', 'Chatham', 'Cotuit', 'Cummaquid', 'Chartley', 'Cuttyhunk',
           'Chepachet', 'Clayville', 'Coventry', 'Central Falls', 'Cumberland', 'Cranston', 'Candia', 'Campton',
           'Canterbury', 'Center Barnstead', 'Center Harbor', 'Center Sandwich', 'Contoocook', 'Chichester',
           'Colebrook', 'Canaan', 'Claremont', 'Cornish', 'Cornish Flat', 'Center Conway', 'Center Ossipee',
           'Center Strafford', 'Center Tuftonboro', 'Chocorua', 'Cape Neddick', 'Cape Porpoise', 'Casco',
           'Center Lovell', 'Chebeague Island', 'Cliff Island', 'Cumberland Center', 'Cape Elizabeth',
           'Cumberland Foreside', 'Coopers Mills', 'Carmel', 'Castine', 'Charleston', 'Corinth', 'Chamberlain',
           'Cushing', 'Calais', 'Cherryfield', 'Columbia Falls', 'Corea', 'Cranberry Isles', 'Cutler', 'Caribou',
           'Clayton Lake', 'Crouseville', 'Camden', 'Caratunk', 'China Village', 'Corinna', 'Cambridgeport',
           'Cavendish', 'Chester Depot', 'Colchester', 'Charlotte', 'Cabot', 'Castleton', 'Center Rutland',
           'Chittenden', 'Cuttingsville', 'Craftsbury', 'Craftsbury Common', 'Canton Center', 'Collinsville', 'Chaplin',
           'Columbia', 'Central Village', 'Centerbrook', 'Cobalt', 'Cromwell', 'Cornwall', 'Cornwall Bridge', 'Cos Cob',
           'Caldwell', 'Carteret', 'Cedar Grove', 'Cliffside Park', 'Clifton', 'Cranford', 'Clark', 'Colonia',
           'Carlstadt', 'Closter', 'Cresskill', 'Cliffwood', 'Colts Neck', 'Califon', 'Changewater', 'Cedar Knolls',
           'Convent Station', 'Cherry Hill', 'Cedar Brook', 'Chatsworth', 'Clarksboro', 'Clementon', 'Columbus',
           'Collingswood', 'Cape May', 'Cape May Court House', 'Cape May Point', 'Cologne', 'Cedarville', 'Clayton',
           'Cookstown', 'Cranbury', 'Cream Ridge', 'Chappaqua', 'Cold Spring', 'Crompond', 'Cross River',
           'Croton Falls', 'Croton On Hudson', 'Cortlandt Manor', 'Campbell Hall', 'Central Valley', 'Circleville',
           'Congers', 'College Point', 'Corona', 'Cambria Heights', 'Carle Place', 'Cedarhurst', 'Centereach',
           'Centerport', 'Central Islip', 'Cold Spring Harbor', 'Commack', 'Copiague', 'Coram', 'Calverton',
           'Center Moriches', 'Cutchogue', 'Caroga Lake', 'Castleton On Hudson', 'Central Bridge', 'Charlotteville',
           'Cherry Plain', 'Clarksville', 'Climax', 'Cobleskill', 'Coeymans', 'Coeymans Hollow', 'Cohoes',
           'Columbiaville', 'Coxsackie', 'Cropseyville', 'Clifton Park', 'Cairo', 'Catskill', 'Connelly',
           'Cornwallville', 'Cottekill', 'Cragsmoor', 'Castle Point', 'Claverack', 'Clinton Corners', 'Clintondale',
           'Copake', 'Copake Falls', 'Cornwall On Hudson', 'Craryville', 'Callicoon', 'Callicoon Center', 'Claryville',
           'Cochecton', 'Cochecton Center', 'Cuddebackville', 'Chestertown', 'Clemons', 'Cleverdale', 'Comstock',
           'Cossayuna', 'Cadyville', 'Champlain', 'Chateaugay', 'Chazy', 'Childwold', 'Churubusco', 'Constable',
           'Cranberry Lake', 'Crown Point', 'Camillus', 'Canastota', 'Cato', 'Cayuga', 'Cazenovia', 'Central Square',
           'Chittenango', 'Cicero', 'Cincinnatus', 'Clay', 'Cleveland', 'Clockville', 'Constantia', 'Cortland',
           'Canajoharie', 'Cassville', 'Chadwicks', 'Clark Mills', 'Cold Brook', 'Constableville', 'Cooperstown',
           'Croghan', 'Calcium', 'Cape Vincent', 'Carthage', 'Castorland', 'Chase Mills', 'Chaumont', 'Chippewa Bay',
           'Colton', 'Copenhagen', 'Candor', 'Castle Creek', 'Chenango Bridge', 'Chenango Forks', 'Colliersville',
           'Conklin', 'Corbettsville', 'Chaffee', 'Clarence', 'Clarence Center', 'Colden', 'Collins', 'Collins Center',
           'Corfu', 'Cowlesville', 'Crittenden', 'Caledonia', 'Canandaigua', 'Castile', 'Churchville', 'Clarendon',
           'Clarkson', 'Clifton Springs', 'Clyde', 'Conesus', 'Caneadea', 'Cassadaga', 'Cattaraugus', 'Celoron',
           'Ceres', 'Chautauqua', 'Cherry Creek', 'Clymer', 'Conewango Valley', 'Cuba', 'Cameron', 'Cameron Mills',
           'Campbell', 'Canaseraga', 'Canisteo', 'Cayuta', 'Chemung', 'Cohocton', 'Coopers Plains', 'Corning',
           'Charleroi', 'Cheswick', 'Clairton', 'Coulters', 'Creighton', 'Cuddy', 'Curtisville', 'Crescent', 'Carnegie',
           'Coraopolis', 'Canonsburg', 'Carmichaels', 'Cecil', 'Claysville', 'Cokeburg', 'Crucible', 'California',
           'Cardale', 'Chalk Hill', 'Chestnut Ridge', 'Coal Center', 'Confluence', 'Connellsville', 'Clearville',
           'Crystal Spring', 'Calumet', 'Champion', 'Claridge', 'Crabtree', 'Carrolltown', 'Chambersville',
           'Cherry Tree', 'Clarksburg', 'Clune', 'Commodore', 'Coolspring', 'Coral', 'Creekside', 'Clarington',
           'Corsica', 'Cairnbrook', 'Cassandra', 'Central City', 'Colver', 'Callery', 'Chicora', 'Connoquenessing',
           'Cranberry Twp', 'Clarks Mills', 'Cadogan', 'Callensburg', 'Clarion', 'Cooksburg', 'Cowansville', 'Crown',
           'Curllsville', 'Carlton', 'Chandlers Valley', 'Cochranton', 'Conneaut Lake', 'Cranberry', 'Clintonville',
           'Cambridge Springs', 'Conneautville', 'Corry', 'Cranesville', 'Calvin', 'Chest Springs', 'Claysburg',
           'Coalport', 'Coupon', 'Cresson', 'Curryville', 'Crosby', 'Custer City', 'Cyclone', 'Centre Hall',
           'Clearfield', 'Coburn', 'Curwensville', 'Columbia Cross Roads', 'Coudersport', 'Covington', 'Camp Hill',
           'Campbelltown', 'Cocolamus', 'Chambersburg', 'Cashtown', 'Codorus', 'Craley', 'Christiana', 'Conestoga',
           'Cammal', 'Castanea', 'Cedar Run', 'Cogan Station', 'Cross Fork', 'Catawissa', 'Coal Township', 'Cressona',
           'Cumbola', 'Catasauqua', 'Center Valley', 'Cherryville', 'Coopersburg', 'Coplay', 'Coaldale', 'Conyngham',
           'Canadensis', 'Cresco', 'Carbondale', 'Chinchilla', 'Clarks Summit', 'Clifford', 'Cambra', 'Camptown',
           'Carversville', 'Chalfont', 'Colmar', 'Cheltenham', 'Chester Heights', 'Clifton Heights', 'Croydon',
           'Crum Lynne', 'Chadds Ford', 'Cheyney', 'Coatesville', 'Cochranville', 'Concordville', 'Cedars',
           'Chester Springs', 'Collegeville', 'Conshohocken', 'Creamery', 'Claymont', 'Camden Wyoming', 'Cheswold',
           'Catlett', 'Centreville', 'Casanova', 'Catharpin', 'Chantilly', 'Callaway', 'Chaptico', 'Charlotte Hall',
           'Clements', 'Cobb Island', 'Coltons Point', 'Compton', 'Capitol Heights', 'Chesapeake Beach', 'Churchton',
           'College Park', 'Chevy Chase', 'Cabin John', 'Chase', 'Cockeysville', 'Crownsville', 'Crofton', 'Curtis Bay',
           'Catonsville', 'Corriganville', 'Church Creek', 'Church Hill', 'Claiborne', 'Cordova', 'Crapo', 'Crocheron',
           'Crumpton', 'Cascade', 'Cavetown', 'Chewsville', 'Clear Spring', 'Cooksville', 'Crisfield', 'Cecilton',
           'Chesapeake City', 'Childs', 'Colora', 'Conowingo', 'Callao', 'Caret', 'Center Cross', 'Coles Point',
           'Colonial Beach', 'Corbin', 'Chester Gap', 'Clear Brook', 'Cross Junction', 'Culpeper', 'Criders',
           'Charlottesville', 'Covesville', 'Crozet', 'Cardinal', 'Cartersville', 'Charles City', 'Christchurch',
           'Church View', 'Cobbs Creek', 'Crozier', 'Cape Charles', 'Capeville', 'Carrollton', 'Carrsville', 'Cheriton',
           'Chesapeake', 'Chincoteague Island', 'Craddockville', 'Capron', 'Carson', 'Church Road', 'Colonial Heights',
           'Courtland', 'Charlotte Court House', 'Chase City', 'Crewe', 'Cullen', 'Christiansburg', 'Catawba', 'Check',
           'Claudville', 'Cloverdale', 'Copper Hill', 'Critz', 'Castlewood', 'Clinchco', 'Clintwood', 'Coeburn', 'Cana',
           'Chilhowie', 'Cripple Creek', 'Crockett', 'Clifton Forge', 'Craigsville', 'Crimora', 'Callands', 'Clover',
           'Cluster Springs', 'Coleman Falls', 'Crystal Hill', 'Cedar Bluff', 'Covel', 'Clear Fork', 'Coal Mountain',
           'Cucumber', 'Cass', 'Crawley', 'Cabin Creek', 'Cannelton', 'Charlton Heights', 'Clear Creek', 'Clendenin',
           'Clothier', 'Colcord', 'Comfort', 'Costa', 'Chloe', 'Cottageville', 'Charles Town', 'Ceredo', 'Chapmanville',
           'Culloden', 'Chauncey', 'Cora', 'Chattaroy', 'Crum', 'Camp Creek', 'Coal City', 'Cool Ridge', 'Corinne',
           'Crab Orchard', 'Charmco', 'Colliers', 'Creston', 'Cowen', 'Camden On Gauley', 'Coalton', 'Center Point',
           'Coxs Mills', 'Crawford', 'Colfax', 'Copen', 'Canvas', 'Capon Bridge', 'Capon Springs', 'Cabins', 'Clemmons',
           'Cooleemee', 'Cedar Falls', 'Cumnock', 'CID', 'Carrboro', 'Cary', 'Chapel Hill', 'Coats', 'Creedmoor',
           'Castalia', 'Chocowinity', 'Como', 'Conetoe', 'Cofield', 'Coinjock', 'Colerain', 'Corapeake', 'Corolla',
           'Creswell', 'Currituck', 'Caroleen', 'Casar', 'China Grove', 'Cliffside', 'Cornelius', 'Cramerton', 'Crouse',
           'Calypso', 'Carolina Beach', 'Castle Hayne', 'Cerro Gordo', 'Chadbourn', 'Clarkton', 'Council', 'Currie',
           'Calabash', 'Cedar Island', 'Chinquapin', 'Cove City', 'Cherry Point', 'Camp Lejeune', 'Collettsville',
           'Connellys Springs', 'Conover', 'Crossnore', 'Crumpler', 'Candler', 'Cashiers', 'Cedar Mountain', 'Cherokee',
           'Chimney Rock', 'Cullowhee', 'Culberson', 'Cassatt', 'Cayce', 'Chapin', 'Chappells', 'Cope', 'Campobello',
           'Chesnee', 'Converse', 'Cowpens', 'Cross Anchor', 'Cross Hill', 'Charleston AFB', 'Canadys', 'Cordesville',
           'Cross', 'Cades', 'Centenary', 'Cheraw', 'Clio', 'Coward', 'Calhoun Falls', 'Central', 'Clemson', 'Conestee',
           'Clarks Hill', 'Clearwater', 'Coosawhatchie', 'Crocketville', 'Conyers', 'Clarkston', 'Cumming', 'Clarkdale',
           'Cave Spring', 'Cedartown', 'Coosa', 'Conley', 'Claxton', 'Cobbtown', 'Chestnut Mountain', 'Canon',
           'Carnesville', 'Cherry Log', 'Clarkesville', 'Clermont', 'Commerce', 'Cornelia', 'Colbert', 'Comer',
           'Crawfordville', 'Calhoun', 'Chickamauga', 'Cisco', 'Cohutta', 'Crandall', 'Camak', 'Cadwell', 'Cordele',
           'Clinchfield', 'Cochran', 'Clyo', 'Camilla', 'Chula', 'Cobb', 'Coolidge', 'Cotton', 'Cataula', 'Cusseta',
           'Callahan', 'Crescent City', 'Citra', 'Carrabelle', 'Chattahoochee', 'Campbellton', 'Caryville', 'Chipley',
           'Cottondale', 'Cypress', 'Cantonment', 'Century', 'Crestview', 'Cedar Key', 'Chiefland', 'Cross City',
           'Casselberry', 'Christmas', 'Clarcona', 'Cape Canaveral', 'Cocoa', 'Cocoa Beach', 'Coral Springs',
           'Coconut Creek', 'Coral Gables', 'Canal Point', 'Clewiston', 'Center Hill', 'Coleman', 'Crystal Springs',
           'Clearwater Beach', 'Cape Coral', 'Captiva', 'Copeland', 'Chokoloskee', 'Cortez', 'Crystal River',
           'Crystal Beach', 'Calera', 'Childersburg', 'Clanton', 'Columbiana', 'Cook Springs', 'Crane Hill', 'Cropwell',
           'Cullman', 'Coaling', 'Coker', 'Carbon Hill', 'Capshaw', 'Centre', 'Crossville', 'Chapman', 'Coosada',
           'Choccolocco', 'Cragford', 'Chancellor', 'Clopton', 'Coffee Springs', 'Cottonwood', 'Cowarts', 'Castleberry',
           'Coy', 'Calvert', 'Chatom', 'Chunchula', 'Citronelle', 'Coden', 'Coffeeville', 'Creola', 'Catherine',
           'Cottonton', 'Castalian Springs', 'Cedar Hill', 'Chapmansboro', 'College Grove', 'Cornersville',
           'Cottontown', 'Cross Plains', 'Cumberland City', 'Cumberland Furnace', 'Cunningham', 'Coalmont',
           'Coker Creek', 'Collegedale', 'Conasauga', 'Copperhill', 'Cowan', 'Chattanooga', 'Chuckey', 'Clairfield',
           'Coalfield', 'Corryton', 'Cosby', 'Cumberland Gap', 'Collierville', 'Crockett Mills', 'Cottage Grove',
           'Counce', 'Crump', 'Chewalla', 'Collinwood', 'Culleoka', 'Cypress Inn', 'Cookeville', 'Campaign', 'Celina',
           'Chestnut Mound', 'Clarkrange', 'Clarksdale', 'Coahoma', 'Coldwater', 'Crenshaw', 'Crowder', 'Calhoun City',
           'Cascilla', 'Coila', 'Cruger', 'Conehatta', 'Chunky', 'Clara', 'Carriere', 'Chatawa', 'Cedarbluff',
           'Calvary', 'Cedar Springs', 'Colquitt', 'Cuthbert', 'Campbellsburg', 'Coxs Creek', 'Crestwood', 'Cloverport',
           'Custer', 'Clay City', 'Cawood', 'Chappell', 'Coalgood', 'Coldiron', 'Cranks', 'Cannon', 'Closplint',
           'Cynthiana', 'Carter', 'Catlettsburg', 'Clayhole', 'Cannel City', 'Canada', 'Carrie', 'Chavies', 'Combs',
           'Cornettsville', 'Cromona', 'Calvert City', 'Crayne', 'Cave City', 'Cadiz', 'Center', 'Cerulean', 'Clifty',
           'Centertown', 'Cleaton', 'Curdsville', 'Corydon', 'Campbellsville', 'Cane Valley', 'Caneyville', 'Canmer',
           'Cecilia', 'Cub Run', 'Cable', 'Centerburg', 'Croton', 'Canal Winchester', 'Carroll', 'Commercial Point',
           'Cardington', 'Carey', 'Chesterville', 'Clay Center', 'Curtice', 'Cygnet', 'Custar', 'Chandlersville',
           'Chesterhill', 'Crooksville', 'Conesville', 'Coshocton', 'Chagrin Falls', 'Chardon', 'Chesterland',
           'Columbia Station', 'Conneaut', 'Chippewa Lake', 'Cuyahoga Falls', 'Canfield', 'Canal Fulton', 'Charm',
           'Chatfield', 'Crestline', 'Cleves', 'College Corner', 'Camp Dennison', 'Chilo', 'Cincinnati', 'Casstown',
           'Chillicothe', 'Cherry Fork', 'Crown City', 'Coal Run', 'Coolville', 'Chickasaw', 'Columbus Grove',
           'Continental', 'Convoy', 'Camby', 'Cedar Lake', 'Chesterton', 'Claypool', 'Culver', 'Columbia City',
           'Corunna', 'Craigville', 'Commiskey', 'Crothersville', 'Cambridge City', 'Connersville', 'Cannelburg',
           'Celestine', 'Crane', 'Chandler', 'Chrisney', 'Carbon', 'Centerpoint', 'Cory', 'Chalmers', 'Crawfordsville',
           'Capac', 'Center Line', 'Clawson', 'Clinton Township', 'Carleton', 'Commerce Township', 'Carsonville',
           'Croswell', 'Chesaning', 'Clare', 'Comins', 'Caro', 'Caseville', 'Cass City', 'Curran', 'Carson City',
           'Cohoctah', 'Crystal', 'Cassopolis', 'Ceresco', 'Coloma', 'Colon', 'Constantine', 'Covert', 'Cement City',
           'Clarklake', 'Cannonsburg', 'Casnovia', 'Comstock Park', 'Coopersville', 'Cadillac', 'Cedar', 'Central Lake',
           'Copemish', 'Carp Lake', 'Charlevoix', 'Cheboygan', 'Cross Village', 'Carney', 'Channing', 'Cooks',
           'Cornell', 'Curtis', 'Caspian', 'Chassell', 'Copper City', 'Copper Harbor', 'Crystal Falls', 'Casey',
           'Chariton', 'Churdan', 'Colo', 'Coon Rapids', 'Cooper', 'Clive', 'Carpenter', 'Clear Lake', 'Corwith',
           'Coulter', 'Crystal Lake', 'Callender', 'Curlew', 'Cylinder', 'Colwell', 'Conrad', 'Castana', 'Cleghorn',
           'Climbing Hill', 'Correctionville', 'Charter Oak', 'Council Bluffs', 'Carter Lake', 'Clarinda', 'Coin',
           'College Springs', 'Colesburg', 'Calmar', 'Center Junction', 'Clutier', 'Coggon', 'Conroy', 'Coralville',
           'Cedar Rapids', 'Cantril', 'Calamus', 'Camanche', 'Columbus City', 'Columbus Junction', 'Campbellsport',
           'Cedarburg', 'Chilton', 'Clyman', 'Colgate', 'Camp Lake', 'Cudahy', 'Cuba City', 'Cambria', 'Combined Locks',
           'Crivitz', 'Chili', 'Colby', 'Curtiss', 'Clam Lake', 'Crandon', 'Camp Douglas', 'Cashton', 'Cataract',
           'Chaseburg', 'Cochrane', 'Coon Valley', 'Cadott', 'Chetek', 'Chippewa Falls', 'Conrath', 'Centuria',
           'Cornucopia', 'Couderay', 'Caroline', 'Cannon Falls', 'Castle Rock', 'Center City', 'Chisago City',
           'Circle Pines', 'Champlin', 'Chanhassen', 'Chaska', 'Cokato', 'Crystal Bay', 'Canyon', 'Chisholm', 'Cloquet',
           'Coleraine', 'Cook', 'Crane Lake', 'Clarks Grove', 'Comfrey', 'Conger', 'Ceylon', 'Canby', 'Chokio',
           'Clara City', 'Clarkfield', 'Clontarf', 'Correll', 'Cosmos', 'Carlos', 'Cyrus', 'Clarissa', 'Crosslake',
           'Clitherall', 'Cass Lake', 'Clearbrook', 'Crookston', 'Canistota', 'Colman', 'Crooks', 'Claire City',
           'Canova', 'Cavour', 'Conde', 'Cresbard', 'Colome', 'Camp Crook', 'Caputa', 'Casselton', 'Christine',
           'Cogswell', 'Cavalier', 'Cummings', 'Cando', 'Churchs Ferry', 'Crary', 'Carrington', 'Cathay', 'Chaseley',
           'Courtenay', 'Cannon Ball', 'Coleharbor', 'Carpio', 'Cartwright', 'Clyde Park', 'Cooke City', 'Crow Agency',
           'Circle', 'Culbertson', 'Capitol', 'Cohagen', 'Colstrip', 'Choteau', 'Coffee Creek', 'Cut Bank', 'Chinook',
           'Canyon Creek', 'Clancy', 'Cardwell', 'Charlo', 'Condon', 'Conner', 'Corvallis', 'Carpentersville',
           'Carol Stream', 'Chicago', 'Crest Hill', 'Calumet City', 'Channahon', 'Chicago Heights', 'Chicago Ridge',
           'Crete', 'Country Club Hills', 'Clarendon Hills', 'Cabery', 'Campus', 'Chebanse', 'Cissna Park',
           'Claytonville', 'Cullom', 'Chadwick', 'Chana', 'Carbon Cliff', 'Coal Valley', 'Colona', 'Cedar Point',
           'Cherry', 'Camp Grove', 'Carman', 'Creve Coeur', 'Carlock', 'Chenoa', 'Congerville', 'Cropsey', 'Catlin',
           'Champaign', 'Collison', 'Camargo', 'Chrisman', 'Coffeen', 'Cottage Hills', 'Carlyle', 'Caseyville',
           'Coulterville', 'Camp Point', 'Coatsburg', 'Colusa', 'Cowden', 'Chestnut', 'Cornland', 'Cantrall',
           'Carlinville', 'Chandlerville', 'Centralia', 'Carmi', 'Christopher', 'Cisne', 'Coello', 'Campbell Hill',
           'Carrier Mills', 'Carterville', 'Cave In Rock', 'Cobden', 'Colp', 'Creal Springs', 'Crystal City',
           'Cottleville', 'Coatsville', 'Cadet', 'Cape Girardeau', 'Canalou', 'Caruthersville', 'Catron', 'Cooter',
           'Clubb', 'Camden Point', 'Centerview', 'Concordia', 'Corder', 'Clearmont', 'Conception',
           'Conception Junction', 'Craig', 'Cainsville', 'Coffey', 'Cowgill', 'Chilhowee', 'Carl Junction', 'Camdenton',
           'Chamois', 'Clifton Hill', 'Climax Springs', 'Cole Camp', 'Cook Sta', 'Crocker', 'Caplinger Mills',
           'Cape Fair', 'Caulfield', 'Cedarcreek', 'Chestnutridge', 'Clever', 'Cross Timbers', 'Cabool', 'Couch',
           'Colony', 'Clearview City', 'Chanute', 'Cassoday', 'Cottonwood Falls', 'Council Grove', 'Cedar Vale',
           'Cheney', 'Colwich', 'Conway Springs', 'Caney', 'Cherryvale', 'Chetopa', 'Coffeyville', 'Cawker City',
           'Claflin', 'Catharine', 'Collyer', 'Cimarron', 'Cedar Bluffs', 'Cedar Creek', 'Clatonia', 'Clarks',
           'Chambers', 'Coleridge', 'Cozad', 'Cody', 'Chadron', 'Chalmette', 'Chauvin', 'Cut Off', 'Cade', 'Carencro',
           'Charenton', 'Chataignier', 'Church Point', 'Crowley', 'Creole', 'Carville', 'Convent', 'Castor',
           'Cotton Valley', 'Coushatta', 'CNB', 'Choudrant', 'Collinston', 'Crowville', 'Cheneyville', 'Cottonport',
           'Campti', 'Cloutierville', 'Crossett', 'Calion', 'Chidester', 'Cale', 'Caddo Gap', 'Cove', 'Casa', 'Casscoe',
           'Center Ridge', 'Choctaw', 'Cotton Plant', 'Crocketts Bluff', 'College Station', 'Clarkedale', 'Colt',
           'Crumrod', 'Caraway', 'Cash', 'Calico Rock', 'Camp', 'Cord', 'Cherokee Village', 'Cushman', 'Clarkridge',
           'Cotter', 'Canehill', 'Cave Springs', 'Centerton', 'Coal Hill', 'Cashion', 'Cement', 'Chickasha', 'Concho',
           'Corn', 'Coyle', 'Cyril', 'Countyline', 'Cache', 'Comanche', 'Canute', 'Cheyenne', 'Cordell', 'Carmen',
           'Carrier', 'Cleo Springs', 'Catoosa', 'Claremore', 'Copan', 'Cardin', 'Chouteau', 'Canadian', 'Checotah',
           'Cookson', 'Council Hill', 'Coweta', 'Centrahoma', 'Clarita', 'Coalgate', 'Caddo', 'Castle', 'Connerville',
           'Coppell', 'Corsicana', 'Copeville', 'Caddo Mills', 'Celeste', 'Chicota', 'Cumby', 'Cookville', 'Cason',
           'Cuney', 'Call', 'Chireno', 'Colmesneil', 'Corrigan', 'Cleburne', 'Colleyville', 'Chico', 'Copperas Cove',
           'China Spring', 'Cranfills Gap', 'Castell', 'Carlsbad', 'Christoval', 'Conroe', 'Coldspring', 'Cedar Lane',
           'Chappell Hill', 'Collegeport', 'Channelview', 'Clute', 'China', 'Chriesman', 'Cuero', 'Calliham',
           'Castroville', 'Cotulla', 'Cibolo', 'Canyon Lake', 'Chapman Ranch', 'Concepcion', 'Corpus Christi', 'CC',
           'Combes', 'Cedar Park', 'Cost', 'Coupland', 'Camp Wood', 'Carrizo Springs', 'Catarina', 'Concan', 'Carmine',
           'Cat Spring', 'Cactus', 'Claude', 'Cotton Center', 'Childress', 'Cee Vee', 'Crowell', 'Crosbyton',
           'Colorado City', 'Coyanosa', 'Canutillo', 'Clint', 'Commerce City', 'Conifer', 'Cowdrey', 'Carr', 'Crook',
           'Calhan', 'Cheyenne Wells', 'Colorado Springs', 'CSOC', 'CMAFB', 'Campo', 'Capulin', 'Chama', 'Chromo',
           'Conejos', 'Creede', 'Crestone', 'Canon City', 'Coal Creek', 'Cotopaxi', 'Crested Butte', 'Cahone',
           'Cedaredge', 'Collbran', 'Centennial', 'Chugwater', 'Cowley', 'Crowheart', 'Casper', 'Cokeville', 'Challis',
           'Conda', 'CSI', 'Castleford', 'Corral', 'Craigmont', 'Culdesac', 'Calder', 'Careywood', 'Cataldo',
           'Clark Fork', 'Clarkia', 'Cocolalla', 'Coeur D Alene', 'CDA', 'Coolin', 'Colburn', 'Cedar Valley',
           'Coalville', 'Cache Junction', 'Castle Dale', 'Centerfield', 'Cannonville', 'Cedar City', 'Casa Grande',
           'Chandler Heights', 'Cave Creek', 'Cibola', 'Congress', 'Carefree', 'Cochise', 'Cortaro', 'Catalina',
           'Cibecue', 'Clay Springs', 'Camp Verde', 'Chino Valley', 'Cornville', 'Crown King', 'Chloride', 'Chinle',
           'Casa Blanca', 'Cedar Crest', 'Cedarvale', 'Cerrillos', 'Claunch', 'Coyote', 'Cubero', 'Counselor',
           'Corrales', 'Clines Corners', 'Cochiti Pueblo', 'Cochiti Lake', 'Church Rock', 'Continental Divide',
           'Crownpoint', 'Canjilon', 'Canones', 'Cebolla', 'Cerro', 'Chamisal', 'Chimayo', 'Costilla', 'Chacon',
           'Caballo', 'Chamberino', 'Cliff', 'Chaparral', 'Clovis', 'Cannon AFB', 'Causey', 'Crossroads', 'Caprock',
           'Carrizozo', 'Capitan', 'Cloudcroft', 'Conchas Dam', 'Cuervo', 'Caliente', 'Coyote Springs', 'Cal Nev Ari',
           'Crescent Valley', 'Carlin', 'Culver City', 'Cerritos', 'Calabasas', 'Canoga Park', 'Castaic',
           'Canyon Country', 'Chino', 'Chino Hills', 'City Of Industry', 'Covina', 'Chula Vista', 'Cardiff By The Sea',
           'Camp Pendleton', 'Coronado', 'Cabazon', 'Calexico', 'Calipatria', 'Cathedral City', 'Coachella', 'Calimesa',
           'Cedar Glen', 'Cedarpines Park', 'Cima', 'Crest Park', 'Capistrano Beach', 'Corona Del Mar', 'Costa Mesa',
           'Camarillo', 'Carpinteria', 'California Hot Springs', 'Camp Nelson', 'Coalinga', 'Corcoran', 'Casmalia',
           'Cayucos', 'California City', 'Cantil', 'Cantua Creek', 'Caruthers', 'Chowchilla', 'Coarsegold',
           'Carmel By The Sea', 'Carmel Valley', 'Chualar', 'Calistoga', 'Castro Valley', 'Corte Madera', 'Cotati',
           'Capitola', 'Cupertino', 'Campo Seco', 'Copperopolis', 'Catheys Valley', 'Chinese Camp', 'Cressey',
           'Crows Landing', 'Calpella', 'Camp Meeker', 'Caspar', 'Cazadero', 'Clearlake', 'Clearlake Oaks',
           'Clearlake Park', 'Comptche', 'Covelo', 'Carlotta', 'Cutten', 'Capay', 'Carmichael', 'Citrus Heights',
           'Cool', 'Camino', 'Chicago Park', 'Camptonville', 'Canyon Dam', 'Cedar Ridge', 'Challenge', 'Clipper Mills',
           'Crescent Mills', 'Cassel', 'Castella', 'Chilcoot', 'Coleville', 'Calpine', 'Carnelian Bay', 'Captain Cook',
           'Camp H M Smith', 'Chuuk', 'Cascade Locks', 'Clackamas', 'Clatskanie', 'Corbett', 'Cannon Beach', 'Cascadia',
           'Camas Valley', 'Canyonville', 'Coos Bay', 'Coquille', 'Central Point', 'Cave Junction', 'Crater Lake',
           'Chiloquin', 'Christmas Valley', 'Camp Sherman', 'Chemult', 'Canyon City', 'Carnation', 'Concrete',
           'Coupeville', 'Camano Island', 'Carbonado', 'Carlsborg', 'Chimacum', 'Clallam Bay', 'Camp Murray',
           'Chehalis', 'Cinebar', 'Copalis Beach', 'Copalis Crossing', 'Cosmopolis', 'Camas', 'Carrolls', 'Cathlamet',
           'Cougar', 'Cashmere', 'Chelan', 'Chelan Falls', 'Conconully', 'Cle Elum', 'Cowiche', 'Chewelah', 'Colville',
           'Coulee City', 'Coulee Dam', 'Cusick', 'College Place', 'Connell', 'Chignik Lake', 'Chefornak', 'Chevak',
           'Chignik', 'Chignik Lagoon', 'Chitina', 'Chugiak', 'Clam Gulch', 'Clarks Point', 'Cold Bay',
           'Cooper Landing',
           'Copper Center', 'Crooked Creek', 'Clear', 'Cantwell', 'Chicken', 'Chalkyitsik', 'Coffman Cove']
DCities = ['Dorado', 'Dalton', 'Deerfield', 'Drury', 'Devens', 'Douglas', 'Dudley', 'Dracut', 'Dunstable', 'Danvers',
           'Dedham', 'Dover', 'Dorchester',
           'Dorchester Center', 'Duxbury', 'Dennis', 'Dennis Port', 'Dartmouth', 'Dighton', 'Derry', 'Dunbarton',
           'Danbury', 'Dublin', 'Drewsville', 'Danville', 'Durham', 'Denmark', 'Dixfield', 'Dryden', 'Dresden',
           'Danforth', 'Dover Foxcroft', 'Damariscotta', 'Deer Isle', 'Dennysville', 'Detroit', 'Dexter', 'Dixmont',
           'Dorset', 'Danby', 'Derby', 'Derby Line', 'Danielson', 'Dayville', 'Deep River', 'Darien', 'Demarest',
           'Dumont', 'Deal', 'Delaware', 'Denville', 'Deepwater', 'Delran', 'Delanco', 'Deptford', 'Dennisville',
           'Deerfield Street', 'Delmont', 'Dividing Creek', 'Dorothy', 'Dayton', 'Dunellen', 'DPO', 'Dobbs Ferry',
           'Deer Park', 'Delanson', 'Delmar', 'Dormansville', 'Duanesburg', 'Denver', 'Dover Plains', 'Diamond Point',
           'Dannemora', 'Dickinson Center', 'Delphi Falls', 'De Ruyter', 'Durhamville', 'Deansboro', 'Dolgeville',
           'Deer River', 'Deferiet', 'De Kalb Junction', 'Depauville', 'De Peyster', 'Davenport', 'Davenport Center',
           'Delancey', 'Delhi', 'Deposit', 'Downsville', 'Dale', 'Darien Center', 'Delevan', 'Depew', 'Dunkirk',
           'Dansville', 'Dewittville', 'Dundee', 'Donora', 'Dravosburg', 'Duquesne', 'Dilliner', 'Daisytown', 'Dawson',
           'Denbo', 'Dickerson Run', 'Dunbar', 'Dunlevy', 'Darragh', 'Donegal', 'De Lancey', 'Dixonville', 'Du Bois',
           'Dagus Mines', 'Driftwood', 'Davidsville', 'Dilltown', 'Dunlo', 'Darlington', 'Distant', 'Defiance',
           'Duncansville', 'Dysart', 'Derrick City', 'De Young', 'Duke Center', 'Drifting', 'Dalmatia', 'Dauphin',
           'Dillsburg', 'Duncannon', 'Doylesburg', 'Dry Run', 'Dallastown', 'Delta', 'Drumore', 'Dewart', 'Dornsife',
           'Danielsville', 'Delano', 'Drifton', 'Drums', 'Delaware Water Gap', 'Dingmans Ferry', 'Damascus', 'Dallas',
           'Dushore', 'Duryea', 'Dimock', 'Doylestown', 'Danboro', 'Darby', 'Dresher', 'Drexel Hill', 'Devon',
           'Downingtown', 'Devault', 'Douglassville', 'Delaware City', 'Dover AFB', 'Dagsboro', 'Dewey Beach', 'Dulles',
           'Delaplane', 'Dhs', 'Dameron', 'Dowell', 'Drayden', 'District Heights', 'Deale', 'Dickerson', 'Derwood',
           'Davidsonville', 'Dundalk', 'Denton', 'Deal Island', 'Dumfries', 'Dunn Loring', 'Dahlgren', 'Dogue',
           'Dunnsville', 'Dyke', 'Deltaville', 'Diggs', 'Doswell', 'Dutton', 'Davis Wharf', 'Dendron', 'Dewitt',
           'Dinwiddie', 'Disputanta', 'Dolphin', 'Drewryville', 'Dillwyn', 'Drakes Branch', 'Dundas', 'Daleville',
           'Dante', 'Duffield', 'Dungannon', 'Draper', 'Dugspur', 'Doe Hill', 'Dry Fork', 'Doran', 'Davy', 'Dunmore',
           'Dawes', 'Deep Water', 'Dixie', 'Drybranch', 'Dry Creek', 'Duck', 'Dunlow', 'Davin', 'Delbarton', 'Dingess',
           'Danese', 'Daniels', 'Dothan', 'Davisville', 'Diana', 'Dailey', 'Davis', 'Dryfork', 'Durbin', 'Dellslow',
           'Dille', 'Drennen', 'Delray', 'Dobson', 'Durants Neck', 'Davidson', 'Dunn', 'Delco', 'Deep Run', 'Deep Gap',
           'Drexel', 'Dana', 'Dillsboro', 'Dalzell', 'Davis Station', 'Drayton', 'Duncan', 'Dillon', 'Donalds',
           'Due West', 'Daufuskie Island', 'Dacula', 'Decatur', 'Duluth', 'Douglasville', 'Daisy', 'Dahlonega',
           'Dawsonville', 'Demorest', 'Dillard', 'Dewy Rose', 'Dearing', 'Davisboro', 'Dry Branch', 'Du Pont',
           'De Soto', 'Doerun', 'Day', 'Doctors Inlet', 'Daytona Beach', 'De Leon Springs', 'Defuniak Springs',
           'Destin', 'Debary', 'Deland', 'Deltona', 'Dania', 'Deerfield Beach', 'Delray Beach', 'Dade City', 'Durant',
           'Dunnellon', 'Dunedin', 'Docena', 'Dolomite', 'Dora', 'Duncanville', 'Double Springs', 'Deatsville',
           'Dozier', 'Daviston', 'De Armanville', 'Dickinson', 'Daphne', 'Dauphin Island', 'Demopolis', 'Dixons Mills',
           'Dadeville', 'Dickson', 'Dixon Springs', 'Dowelltown', 'Decherd', 'Ducktown', 'Dunlap', 'Dandridge',
           'Deer Lodge', 'Del Rio', 'Duff', 'Drummonds', 'Dyersburg', 'Dukedom', 'Darden', 'Decaturville', 'Dyer',
           'Dellrose', 'Duck River', 'Doyle', 'Darling', 'Dumas', 'DSU', 'Doddsville', 'Drew', 'Derma', 'Duck Hill',
           'Delta City', 'D Lo', 'De Kalb', 'Diamondhead', 'Diberville', 'Donalsonville', 'Denniston', 'Dayhoit',
           'De Mossville', 'Dry Ridge', 'Debord', 'Dorton', 'David', 'Drift', 'Dwale', 'Delphia', 'Dice', 'Dwarf',
           'Deane', 'Dema', 'Dycusburg', 'Drake', 'Drakesboro', 'Dunmor', 'Dawson Springs', 'Dixon', 'Dunnville',
           'Dubre', 'De Graff', 'Dunbridge', 'Deshler', 'Derwent', 'Duncan Falls', 'Dillonvale', 'Diamond', 'Dellroy',
           'Dennison', 'Deersville', 'Donnelsville', 'Dexter City', 'Delphos', 'Dola', 'Dupont', 'Demotte', 'Donaldson',
           'Deedsville', 'Delong', 'Delphi', 'Depauw', 'Deputy', 'Dunreith', 'Decker', 'Dubois', 'Dugger', 'Dearborn',
           'Dearborn Heights', 'DTE', 'Drayton Plains', 'Davisburg', 'Davison', 'Deckerville', 'Durand', 'Deford',
           'Dimondale', 'Delton', 'Dowagiac', 'Dowling', 'Dorr', 'Dafter', 'De Tour Village', 'Drummond Island',
           'Daggett', 'Deerton', 'Dodgeville', 'Dollar Bay', 'Dallas Center', 'Davis City', 'Dows', 'Des Moines',
           'Dougherty', 'Dakota City', 'Dolliver', 'Duncombe', 'Dewar', 'Dike', 'Dunkerton', 'Diagonal', 'Doon',
           'Dickens', 'Deloit', 'Denison', 'Dow City', 'Dubuque', 'Durango', 'Dyersville', 'Decorah', 'Douds',
           'Drakesville', 'Donnellson', 'De Witt', 'Donahue', 'Delafield', 'Delavan', 'Dousman', 'Dane', 'De Forest',
           'Dickeyville', 'Dellwood', 'Dresser', 'De Pere', 'Deerbrook', 'Dodge', 'Downing', 'Drummond', 'Dalbo',
           'Darwin', 'Dassel', 'Dakota', 'Dodge Center', 'Darfur', 'Dovray', 'Dunnell', 'Danube', 'Donnelly',
           'Deerwood', 'Detroit Lakes', 'Deer Creek', 'Dent', 'Dilworth', 'Dell Rapids', 'De Smet', 'Doland', 'Dupree',
           'Deadwood', 'Dahlen', 'Devils Lake', 'Dunseith', 'Dazey', 'Denhoff', 'Dickey', 'Driscoll', 'Dunn Center',
           'Deering', 'Des Lacs', 'Donnybrook', 'Dagmar', 'Dupuyer', 'Dodson', 'Dell', 'Divide', 'De Borgia',
           'Des Plaines', 'Dekalb', 'Dolton', 'Dwight', 'Downers Grove', 'Donovan', 'Davis Junction', 'Deer Grove',
           'Depue', 'Dahinda', 'Dunfermline', 'Downs', 'De Land', 'Dewey', 'Dalton City', 'Dorsey', 'Dow', 'Dupo',
           'Dallas City', 'Dieterich', 'Divernon', 'Dix', 'Du Quoin', 'Dongola', 'Dittmer', 'Dutzow', 'Des Arc',
           'Doe Run', 'Dutchtown', 'Doniphan', 'Dawn', 'Duenweg', 'Devils Elbow', 'Duke', 'Diggins', 'Dunnegan',
           'Delia', 'Douglass', 'Damar', 'Dorrance', 'Dodge City', 'Davey', 'Daykin', 'Diller', 'David City',
           'Dannebrog', 'Dunning', 'Deweese', 'Des Allemands', 'Destrehan', 'Donaldsonville', 'Donner', 'Dulac',
           'Delcambre', 'Duson', 'Dequincy', 'Deridder', 'Denham Springs', 'Darrow', 'Duplessis', 'Doyline', 'Dubberly',
           'Dubach', 'Deville', 'Dry Prong', 'Dermott', 'De Queen', 'Dierks', 'Doddridge', 'Delight', 'De Valls Bluff',
           'Diaz', 'Driver', 'Dyess', 'Datto', 'Delaplaine', 'Desha', 'Dolph', 'Drasco', 'Deer', 'Dennard',
           'Diamond City', 'Dardanelle', 'Dibble', 'Devol', 'Dill City', 'Dacoma', 'Drumright', 'Disney', 'Dustin',
           'Desoto', 'DFW', 'Deport', 'Dodd City', 'Daingerfield', 'De Berry', 'Donie', 'Diboll', 'Doucette', 'De Leon',
           'Desdemona', 'Davilla', 'Doole', 'Dallardsville', 'Dobbin', 'Damon', 'Danciger', 'Danevang', 'Daisetta',
           'Devers', 'Deweyville', 'Deanville', 'Dime Box', 'Devine', 'Dilley', 'Dinero', 'Delmita', 'Donna',
           'Del Valle', 'Doss', 'Dripping Springs', 'D Hanis', 'Dalhart', 'Darrouzett', 'Dimmitt', 'Denver City',
           'Dyess AFB', 'Dell City', 'Deer Trail', 'Dacono', 'Del Norte', 'Dolores', 'Dove Creek', 'Dinosaur',
           'De Beque', 'Deaver', 'Devils Tower', 'Daniel', 'Diamondville', 'Dingle', 'Downey', 'Declo', 'Dietrich',
           'Driggs', 'Deary', 'Desmet', 'Duchesne', 'Dugway', 'Dutch John', 'Duck Creek Village', 'Dammeron Valley',
           'Dateland', 'Dragoon', 'DM AFB', 'Dolan Springs', 'Dennehotso', 'Dulce', 'Datil', 'Deming', 'Dona Ana',
           'Duckwater', 'Denio', 'Deeth', 'Dodgertown', 'Duarte', 'Diamond Bar', 'Descanso', 'Dulzura', 'Del Mar',
           'Desert Center', 'Desert Hot Springs', 'Death Valley', 'Dana Point', 'Ducor', 'Del Rey', 'Dinuba',
           'Dos Palos', 'Daly City', 'Discovery Bay', 'Diablo', 'Dillon Beach', 'Douglas Flat', 'Denair', 'Dos Rios',
           'Duncans Mills', 'Diamond Springs', 'Drytown', 'Dutch Flat', 'Dobbins', 'Downieville', 'Dunnigan', 'Dorris',
           'Douglas City', 'Dunsmuir', 'Davis Creek', 'Dededo', 'Donald', 'Dufur', 'Deer Island', 'Depoe Bay',
           'Days Creek', 'Dorena', 'Drain', 'Dairy', 'Drewsey', 'Durkee', 'Duvall',
           'Darrington', 'Deer Harbor', 'Doty', 'Dallesport', 'Dillingham', 'Dutch Harbor', 'Delta Junction',
           'Denali National Park']
ECities = ['Ensenada', 'Easthampton', 'East Longmeadow', 'East Otis', 'Erving', 'East Templeton', 'East Brookfield',
           'East Princeton', 'EMC',
           'Essex', 'East Walpole', 'Everett', 'East Weymouth', 'East Boston', 'East Bridgewater', 'Easton', 'Elmwood',
           'East Falmouth', 'East Sandwich',
           'East Wareham', 'Edgartown', 'East Dennis', 'Eastham', 'East Orleans', 'East Freetown', 'East Taunton',
           'East Greenwich', 'Exeter', 'East Providence', 'East Candia', 'East Derry', 'Epping', 'East Andover',
           'Elkins', 'Epsom', 'Errol', 'Enfield', 'Enfield Center', 'Etna', 'East Hampstead', 'East Kingston',
           'East Wakefield', 'Eaton Center', 'Effingham', 'Eliot', 'East Baldwin', 'East Parsonsfield',
           'East Waterboro', 'East Dixfield', 'East Livermore', 'East Poland', 'East Wilton', 'East Winthrop',
           'Eddington', 'East Millinocket', 'East Orland', 'East Boothbay', 'Edgecomb', 'Ellsworth', 'East Blue Hill',
           'East Machias', 'Eastport', 'Eagle Lake', 'Estcourt Station', 'East Newport', 'East Vassalboro', 'Eustis',
           'East Corinth', 'East Randolph', 'East Ryegate', 'East Thetford', 'East Arlington', 'East Dorset',
           'East Dover', 'East Berkshire', 'East Fairfield', 'Enosburg Falls', 'Essex Junction', 'East Barre',
           'East Calais', 'East Montpelier', 'Eden', 'Eden Mills', 'East Middlebury', 'East Poultney',
           'East Wallingford', 'East Burke', 'East Charleston', 'East Hardwick', 'East Haven', 'East Saint Johnsbury',
           'East Berlin', 'East Canaan', 'East Glastonbury', 'East Granby', 'East Hartland', 'East Windsor Hill',
           'Ellington', 'East Windsor', 'East Hartford', 'Eastford', 'East Killingly', 'East Woodstock', 'East Lyme',
           'East Haddam', 'East Hampton', 'East Orange', 'Edgewater', 'Essex Fells', 'East Rutherford', 'Elizabeth',
           'Elizabethport', 'Elmwood Park', 'Emerson', 'Englewood', 'Englewood Cliffs', 'Eatontown', 'Englishtown',
           'East Hanover', 'Ewan', 'Egg Harbor City', 'Elwood', 'Egg Harbor Township', 'Elmer', 'Estell Manor',
           'East Brunswick', 'Edison', 'Elmsford', 'Eastchester', 'Elmont', 'East Elmhurst', 'Elmhurst',
           'East Rockaway', 'East Meadow', 'East Islip', 'East Northport', 'East Norwich', 'East Setauket',
           'East Marion', 'East Moriches', 'East Quogue', 'Eagle Bridge', 'Earlton', 'East Berne', 'East Chatham',
           'East Greenbush', 'East Nassau', 'East Schodack', 'East Worcester', 'Esperance', 'East Durham',
           'East Jewett', 'Elka Park', 'Ellenville', 'Esopus', 'Elizaville', 'Eldred', 'Elizabethtown', 'Ellenburg',
           'Ellenburg Center', 'Ellenburg Depot', 'East Homer', 'East Syracuse', 'Elbridge', 'Erieville', 'Eagle Bay',
           'Earlville', 'East Springfield', 'Eaton', 'Edmeston', 'Edwards', 'Ellisburg', 'Evans Mills', 'East Branch',
           'East Meredith', 'East Pharsalia', 'Endicott', 'Endwell', 'East Amherst', 'East Aurora', 'East Bethany',
           'East Concord', 'East Pembroke', 'Elba', 'Elma', 'East Bloomfield', 'East Rochester', 'East Williamson',
           'East Otto', 'Ellicottville', 'Erin', 'Elmira', 'East Mc Keesport', 'Elrama', 'East Pittsburgh',
           'Eighty Four', 'East Millsboro', 'Elco', 'East Vandergrift', 'Everson', 'Export', 'Elderton', 'Elmora',
           'Emeigh', 'Ernest', 'Emporium', 'Ebensburg', 'Elton', 'East Brady', 'East Butler', 'Eau Claire',
           'Evans City', 'Edinburg', 'Ellwood City', 'Enon Valley', 'East Hickory', 'Endeavor', 'Emlenton', 'Edinboro',
           'Elgin', 'Erie', 'East Freedom', 'Entriken', 'East Smethport', 'Elkland', 'East Waterford', 'Elizabethville',
           'Elliottsburg', 'Enola', 'East Prospect', 'Emigsville', 'Etters', 'East Earl', 'East Petersburg', 'Elm',
           'Ephrata', 'Eagles Mere', 'Elysburg', 'East Greenville', 'East Texas', 'Emmaus', 'Ebervale',
           'East Stroudsburg', 'Effort', 'Equinunk', 'East Smithfield', 'Earlington', 'Erwinna', 'Elkins Park',
           'Edgemont', 'Essington', 'Exton', 'Eagleville', 'Elverson', 'Ellendale', 'Edgewood', 'Ellicott City',
           'Elkridge', 'Eckhart Mines', 'Ellerslie', 'East New Market', 'Emmitsburg', 'Ewell', 'Earleville',
           'Elk Mills', 'Elkton', 'Edwardsville', 'Elkwood', 'Etlan', 'Earlysville', 'Esmont', 'Eastville', 'Exmore',
           'Ebony', 'Elberon', 'Emporia', 'Evergreen', 'Eagle Rock', 'Eggleston', 'Elliston', 'East Stone Gap', 'Ewing',
           'Elk Creek', 'Emory', 'Evington', 'Eckman', 'Elbert', 'Elkhorn', 'East Bank', 'Eleanor', 'Elkview',
           'Eskdale', 'Ethel', 'Evans', 'East Lynn', 'Edgarton', 'Eccles', 'Edmond', 'Erbacon', 'Ellamore', 'Ellenboro',
           'Enterprise', 'Exchange', 'Eglon', 'Elk Garden', 'East Bend', 'Eagle Springs', 'Efland', 'Elon', 'Ether',
           'Edward', 'Elm City', 'Engelhard', 'Everetts', 'Elizabeth City', 'Edenton', 'Eure', 'Earl', 'East Spencer',
           'Ellerbe', 'Erwin', 'Ernul', 'Emerald Isle', 'Elkin', 'Elk Park', 'Ennice', 'East Flat Rock', 'Edneyville',
           'Enka', 'Etowah', 'Eastover', 'Elliott', 'Elloree', 'Eutawville', 'Ehrhardt', 'Enoree', 'Edisto Island',
           'Easley', 'Edgemoor', 'Edgefield', 'Elko', 'Early Branch', 'Estill', 'Esom Hill', 'Experiment', 'Ellenwood',
           'Ellijay', 'Eastanollee', 'East Ellijay', 'Epworth', 'Elberton', 'Eton', 'Eastman', 'Eatonton',
           'East Dublin', 'Ellabell', 'Ellenton', 'Enigma', 'Ellaville', 'East Palatka', 'Eastlake Weir', 'Edgar',
           'Eastpoint', 'Ebro', 'Eglin AFB', 'Earleton', 'Evinston', 'Eaton Park', 'El Jobean', 'Estero',
           'Everglades City', 'Elfers', 'Empire', 'Echola', 'Elrod', 'Emelle', 'Epes', 'Ethelsville', 'Eutaw',
           'Eldridge', 'Elkmont', 'Eva', 'Estillfork', 'East Tallassee', 'Eclectic', 'Elmore', 'Equality', 'Eufaula',
           'Eastaboga', 'Excel', 'Elberta', 'Eight Mile', 'Elora', 'Estill Springs', 'Evensville', 'ETSU',
           'Elizabethton', 'Eagan', 'Eidson', 'Eads', 'Enville', 'Ethridge', 'Etta', 'Ecru', 'Enid', 'Eastabuchie',
           'Ellisville', 'Escatawpa', 'Eupora', 'Eastwood', 'Eminence', 'Ekron', 'Elliottville', 'East Bernstadt',
           'Emlyn', 'Eolia', 'Essie', 'Evarts', 'Erlanger', 'East Point', 'Elkfork', 'Ezel', 'Elkhorn City', 'Eastern',
           'Emmalena', 'Ermine', 'Eddyville', 'Edmonton', 'Eighty Eight', 'Etoile', 'Eubank', 'Eastview', 'Elk Horn',
           'East Liberty', 'Edgerton', 'Edon', 'Evansport', 'East Fultonham', 'East Liverpool', 'East Claridon',
           'Elyria', 'Eastlake', 'Euclid', 'East Palestine', 'East Sparta', 'East Canton', 'Eldorado', 'Enon',
           'Edinburgh', 'East Chicago', 'Elkhart', 'Etna Green', 'East Enterprise', 'Eckerty', 'English', 'Economy',
           'Ellettsville', 'Edwardsport', 'Elnora', 'Evanston', 'Elberfeld', 'Evansville', 'Earl Park', 'Eastpointe',
           'Emmett', 'East China', 'Ecorse', 'Edenville', 'East Tawas', 'Essexville', 'Eagle', 'East Lansing',
           'Eaton Rapids', 'Edmore', 'Elm Hall', 'Elsie', 'Elwell', 'Eureka', 'East Leroy', 'Edwardsburg', 'Elk Rapids',
           'Evart', 'East Jordan', 'Eckerman', 'Eben Junction', 'Engadine', 'Escanaba', 'Ewen', 'Earlham', 'Ellston',
           'Exira', 'Eagle Grove', 'Early', 'Emmetsburg', 'Eldora', 'Evansdale', 'Estherville', 'Everly', 'Earling',
           'Elkader', 'Elkport', 'Ely', 'Eldon', 'Exline', 'Elkhart Lake', 'East Troy', 'Elm Grove', 'Edmund', 'Elroy',
           'East Ellsworth', 'Egg Harbor', 'Ellison Bay', 'Ephraim', 'Eland', 'Elcho', 'Elderon', 'Eagle River',
           'Ettrick', 'Eau Galle', 'Eleva', 'Elk Mound', 'Exeland', 'Embarrass', 'Elko New Market', 'Eden Valley',
           'Elk River', 'Excelsior', 'Eden Prairie', 'Esko', 'Eveleth', 'Eitzen', 'Eyota', 'Elysian', 'Emmons', 'Essig',
           'Echo', 'Elrosa', 'Eagle Bend', 'Emily', 'Elbow Lake', 'Erhard', 'Erskine', 'Effie', 'East Grand Forks',
           'Egan', 'Elk Point', 'Estelline', 'Emery', 'Ethan', 'Eagle Butte', 'Ellsworth AFB', 'Enning', 'Enderlin',
           'Emerado', 'Egeland', 'Esmond', 'Edgeley', 'Emigrant', 'Ekalaka', 'East Glacier Park', 'East Helena',
           'Ennis', 'Elmo', 'Elk Grove Village', 'Elburn', 'Eola', 'Evergreen Park', 'Emington', 'East Dubuque',
           'Eleroy', 'East Moline', 'Eldena', 'East Galesburg', 'Edelstein', 'East Peoria', 'El Paso', 'Eagarville',
           'East Alton', 'Elsah', 'East Saint Louis', 'East Carondelet', 'Ellis Grove', 'Elvaston', 'Elwin', 'Emden',
           'Ellery', 'Emma', 'Elkville', 'Energy', 'Earth City', 'Elsberry', 'Edina', 'East Prairie', 'Ellsinore',
           'Excelsior Springs', 'East Lynne', 'El Dorado Springs', 'Eugene', 'Excello', 'Edgar Springs', 'Eunice',
           'Eudora', 'Everton', 'Eskridge', 'Everest', 'Elsmore', 'Elmdale', 'Esbon', 'Elbing', 'El Dorado', 'Edna',
           'Elk City', 'Elk Falls', 'Ellinwood', 'Ellis', 'Edson', 'Ensign', 'Ericson', 'Emmet', 'Elm Creek', 'Enders',
           'Elsmere', 'Edgard', 'Erath', 'Estherwood', 'Evangeline', 'Erwinville', 'Epps', 'Eros', 'England', 'Earle',
           'Edmondson', 'Elaine', 'Egypt', 'Evening Shade', 'Eureka Springs', 'Elm Springs', 'Eakly', 'El Reno',
           'Elmore City', 'Erick', 'Eucha', 'Eagletown', 'Earlsboro', 'Eustace', 'Ector', 'Enloe', 'Elysian Fields',
           'Euless', 'Era', 'Electra', 'Eastland', 'Eddy', 'Evant', 'Elm Mott', 'East Bernard', 'El Campo', 'Elmaton',
           'Evadale', 'Encinal', 'Ecleto', 'Elmendorf', 'Edroy', 'Encino', 'Edcouch', 'Elsa', 'Eagle Pass', 'El Indio',
           'Ellinger', 'Earth', 'Edmonson', 'Enochs', 'Eldorado Springs', 'Estes Park', 'Eckley', 'Egnar', 'Eckert',
           'Elk Mountain', 'Encampment', 'Emblem', 'Eagle Mountain', 'East Carbon', 'Elsinore', 'Escalante', 'Eloy',
           'Ehrenberg', 'El Mirage', 'Elfrida', 'Eagar', 'Estancia', 'El Prado', 'El Rito', 'Embudo', 'Espanola',
           'Eagle Nest', 'Elephant Butte', 'Elida', 'El Segundo', 'El Monte', 'El Cajon', 'Encinitas', 'Escondido',
           'Earp', 'El Centro', 'El Toro', 'East Irvine', 'Earlimart', 'El Granada', 'El Cerrito', 'Emeryville',
           'El Sobrante', 'El Nido', 'El Portal', 'Escalon', 'Elk', 'El Verano', 'Elk Grove', 'Elverta', 'Esparto',
           'Emigrant Gap', 'Echo Lake', 'El Dorado Hills', 'Eleele', 'Ewa Beach', 'Ebeye', 'Eagle Creek', 'Estacada',
           'Eagle Point', 'Edmonds', 'Enumclaw', 'Eastsound', 'Eatonville', 'Elbe', 'East Olympia', 'East Wenatchee',
           'Entiat', 'Ellensburg', 'Edwall',
           'Electric City', 'Elmer City', 'Eltopia', 'Eek', 'Egegik', 'Ekwok', 'Emmonak', 'Eielson AFB', 'Ester',
           'Elim', 'Elfin Cove']
FCities = ['Florida', 'Fajardo', 'Frederiksted', 'Fort Buchanan', 'Feeding Hills', 'Florence', 'Fitchburg', 'Fiskdale',
           'Framingham', 'Fayville',
           'Foxboro', 'Franklin', 'Falmouth', 'Forestdale', 'Fairhaven', 'Fall River', 'Fiskeville', 'Foster',
           'Francestown', 'Fremont', 'Fitzwilliam',
           'Franconia', 'Farmington', 'Freedom', 'Freeport', 'Fryeburg', 'Farmingdale', 'Frankfort', 'Friendship',
           'Frenchboro', 'Fort Fairfield', 'Fort Kent',
           'Fort Kent Mills', 'Frenchville', 'Fairfield', 'Farmington Falls', 'Fairlee', 'Fairfax', 'Ferrisburgh',
           'Fair Haven', 'Forest Dale', 'Falls Village', 'Fabyan', 'Fishers Island', 'Fairview', 'Fanwood', 'Fort Lee',
           'Fair Lawn', 'Franklin Lakes', 'Fort Monmouth', 'Freehold', 'Flanders', 'Far Hills', 'Florham Park',
           'Fairton', 'Fortescue', 'Franklinville', 'Fort Dix', 'Forked River', 'Flagtown', 'Flemington',
           'Franklin Park', 'Frenchtown', 'Fords', 'FPO', 'Fort Montgomery', 'Floral Park', 'Franklin Square',
           'Flushing', 'Fresh Meadows', 'Forest Hills', 'Far Rockaway', 'Farmingville', 'Feura Bush', 'Fonda',
           'Fort Hunter', 'Fort Johnson', 'Fultonham', 'Fultonville', 'Fleischmanns', 'Fishkill', 'Fallsburg',
           'Ferndale', 'Fremont Center', 'Forestburgh', 'Fort Ann', 'Fort Edward', 'Fort Covington', 'Fabius',
           'Fayette', 'Fayetteville', 'Freeville', 'Fulton', 'Fly Creek', 'Forestport', 'Fort Plain',
           'Franklin Springs', 'Fort Drum', 'Felts Mills', 'Fine', 'Fishers Landing', 'Fishs Eddy',
           'Farmersville Station', 'Farnham', 'Forestville', 'Fredonia', 'Fairport', 'Fancher', 'Fishers', 'Falconer',
           'Fillmore', 'Findley Lake', 'Frewsburg', 'Finleyville', 'Fredericktown', 'Fairbank', 'Fairchance',
           'Fayette City', 'Fairhope', 'Fishertown', 'Fort Hill', 'Friedens', 'Forbes Road', 'Falls Creek', 'Force',
           'Fenelton', 'Foxburg', 'Farrell', 'Fombell', 'Fairmount City', 'Fisher', 'Ford City', 'Ford Cliff',
           'Fryburg', 'Fallentimber', 'Flinton', 'Fleming', 'Fredericksburg', 'Fannettsburg', 'Fort Littleton',
           'Fort Loudon', 'Fawn Grove', 'Felton', 'Franklintown', 'Freeburg', 'Frackville', 'Friedensburg',
           'Flicksville', 'Fogelsville', 'Freeland', 'Factoryville', 'Fleetville', 'Forest City', 'Falls', 'Forksville',
           'Friendsville', 'Forest Grove', 'Fountainville', 'Furlong', 'Fairless Hills', 'Flourtown', 'Folcroft',
           'Folsom', 'Fort Washington', 'Feasterville Trevose', 'Fairview Village', 'Frederick', 'Fleetwood',
           'Fenwick Island', 'Frankford', 'Frederica', 'FBI', 'Faulkner', 'Fort George G Meade', 'Fallston',
           'Finksburg', 'Forest Hill', 'Fork', 'Fort Howard', 'Flintstone', 'Frostburg', 'Federalsburg',
           'Fishing Creek', 'Fairplay', 'Funkstown', 'Fruitland', 'Fairfax Station', 'Falls Church', 'Fort Belvoir',
           'Fort Myer', 'FDIC', 'Fishers Hill', 'Flint Hill', 'Front Royal', 'Fort Valley', 'Fulks Run', 'Faber',
           'Fishersville', 'Free Union', 'Fork Union', 'Franktown', 'Fort Eustis', 'Fort Monroe', 'Ford', 'Freeman',
           'Farmville', 'Fort Mitchell', 'Ferrum', 'Fieldale', 'Fincastle', 'Floyd', 'Fort Blackmore', 'Fancy Gap',
           'Fries', 'Fort Defiance', 'Forest', 'Falls Mills', 'Fanrock', 'Fairlea', 'Falling Rock', 'Fraziers Bottom',
           'Falling Waters', 'Fort Gay', 'Fairdale', 'Flat Top', 'Follansbee', 'Friendly', 'Fenwick', 'French Creek',
           'Frenchton', 'Fairmont', 'Four States', 'Flatwoods', 'Frametown', 'Fort Ashby', 'Four Oaks', 'Franklinton',
           'Fuquay Varina', 'Falkland', 'Fountain', 'Frisco', 'Faith', 'Fort Bragg', 'Faison', 'Falcon', 'Fair Bluff',
           'Ferguson', 'Flat Rock', 'Fletcher', 'Fontana Dam', 'Fairforest', 'Fingerville', 'Folly Beach', 'Fair Play',
           'Fountain Inn', 'Fort Mill', 'Fort Lawn', 'Furman', 'Fairmount', 'Fairburn', 'Flovilla', 'Forest Park',
           'Flowery Branch', 'Fort Oglethorpe', 'Forsyth', 'Fort Stewart', 'Folkston', 'Fargo', 'Fitzgerald', 'Funston',
           'Fortson', 'Fort Benning', 'Fleming Island', 'Fernandina Beach', 'Fort White', 'Fort Mc Coy',
           'Flagler Beach', 'Florahome', 'Fort Walton Beach', 'Fellsmere', 'Fort Lauderdale', 'Fort Meade',
           'Frostproof', 'Fort Myers', 'FMY', 'F M', 'Felda', 'Fort Myers Beach', 'Fort Ogden', 'Floral City',
           'Fruitland Park', 'Fort Pierce', 'Fultondale', 'Fosters', 'Falkville', 'Fackler', 'Fort Payne', 'Fyffe',
           'Fitzpatrick', 'Forest Home', 'Fort Davis', 'Fort Deposit', 'Fruithurst', 'Fort Rucker', 'Flomaton',
           'Florala', 'Frisco City', 'Foley', 'Frankville', 'Fruitdale', 'Faunsdale', 'Forkland', 'Five Points',
           'Fosterville', 'Farner', 'Flintville', 'Fall Branch', 'Flag Pond', 'Finley', 'Finger', 'Fruitvale',
           'Frankewing', 'Falkner', 'Friars Point', 'Flora', 'Flowood', 'Foxworth', 'Fernwood', 'French Camp',
           'Fort Gaines', 'Fowlstown', 'Finchville', 'Fisherville', 'Falls Of Rough', 'Fort Knox', 'Farmers',
           'Frenchburg', 'Fall Rock', 'Flat Lick', 'Fourmile', 'Frakes', 'Ft Mitchell', 'Flemingsburg', 'Fort Thomas',
           'Flatgap', 'Fedscreek', 'Fords Branch', 'Freeburn', 'Fisty', 'Fancy Farm', 'Fountain Run', 'Fort Campbell',
           'Fordsville', 'Farmer', 'Frazeysburg', 'Fresno', 'Fairpoint', 'Fairlawn', 'Farmdale', 'Fowler', 'Fostoria',
           'Feesburg', 'Felicity', 'Fairborn', 'Farmersville', 'Franklin Furnace', 'Findlay', 'Fort Jennings',
           'Fort Loramie', 'Fort Recovery', 'Fortville', 'Frankton', 'Fairland', 'Finly', 'Fountaintown', 'Fort Wayne',
           'Fowlerton', 'Floyds Knobs', 'Freetown', 'Farmland', 'Fountain City', 'French Lick', 'Ferdinand',
           'Freelandville', 'Fulda', 'Fort Branch', 'Francisco', 'Fairbanks', 'Farmersburg', 'Fontanet', 'Fair Oaks',
           'Francesville', 'Fraser', 'Fort Gratiot', 'Fenton', 'Filion', 'Flint', 'Farwell', 'Fairgrove', 'Frankenmuth',
           'Fowlerville', 'Frontier', 'Fennville', 'Ferrysburg', 'Free Soil', 'Fruitport', 'Fife Lake', 'Filer City',
           'Frederic', 'Felch', 'Foster City', 'Fertile', 'Fort Dodge', 'Farnhamville', 'Frederika', 'Fontanelle',
           'Farragut', 'Farley', 'Fort Atkinson', 'Floris', 'Fort Madison', 'Fontana', 'Franksville', 'Footville',
           'Fennimore', 'Fairwater', 'Fox Lake', 'Friesland', 'Fence', 'Forest Junction', 'Fish Creek', 'Francis Creek',
           'Fifield', 'Ferryville', 'Fairchild', 'Fall Creek', 'Fond Du Lac', 'FDL', 'Faribault', 'Forest Lake',
           'Frontenac', 'Finland', 'Finlayson', 'Floodwood', 'Forbes', 'Freeborn', 'Frost', 'Flensburg', 'Foreston',
           'Fifty Lakes', 'Fort Ripley', 'Fergus Falls', 'Flom', 'Fosston', 'Foxhome', 'Frazee', 'Federal Dam',
           'Flandreau', 'Fedora', 'Fort Thompson', 'Faulkton', 'Ferney', 'Fort Pierre', 'Fingal', 'Forman',
           'Fort Ransom', 'Fordville', 'Forest River', 'Fort Totten', 'Fessenden', 'Fullerton', 'Flasher', 'Fort Yates',
           'Flaxton', 'Fortuna', 'Fishtail', 'Fromberg', 'Fort Smith', 'Flaxville', 'Fort Peck', 'Frazer', 'Froid',
           'Fallon', 'Floweree', 'Fort Benton', 'Fort Shaw', 'Fort Harrison', 'Fortine', 'Fox River Grove',
           'Fort Sheridan', 'Flossmoor', 'Fox Valley', 'Forreston', 'Franklin Grove', 'Fiatt', 'Fairbury', 'Flanagan',
           'Forrest', 'Farmer City', 'Fithian', 'Foosland', 'Fidelity', 'Fieldon', 'Fairview Heights', 'Fults',
           'Ferris', 'Farina', 'Frankfort Heights', 'Freeman Spur', 'Festus', 'Florissant', 'French Village', 'Farber',
           'Flinthill', 'Foristell', 'Farrar', 'Friedheim', 'Frohna', 'Fagus', 'Fairdealing', 'Fisk', 'Faucett',
           'Fort Leonard Wood', 'Fair Grove', 'Fordland', 'Freistatt', 'Fort Leavenworth', 'Fort Riley', 'Fort Scott',
           'Farlington', 'Formoso', 'Falun', 'Fort Calhoun', 'Falls City', 'Filley', 'Firth', 'Friend', 'Fordyce',
           'Funk', 'Farnam', 'Fluker', 'Fordoche', 'French Settlement', 'Frierson', 'Farmerville', 'Fort Necessity',
           'Ferriday', 'Florien', 'Fort Polk', 'Fountain Hill', 'Foreman', 'Fouke', 'Fox', 'Fairfield Bay',
           'Forrest City', 'Frenchmans Bayou', 'Fifty Six', 'Floral', 'Flippin', 'Fort Cobb', 'Fort Sill', 'Faxon',
           'Fay', 'Foss', 'Fort Supply', 'Felt', 'Forgan', 'Foyil', 'Fort Gibson', 'Fort Towson', 'Fittstown',
           'Fitzhugh', 'Francis', 'Fanshawe', 'Flower Mound', 'Forney', 'Fate', 'Frankston', 'Fort Worth', 'Forestburg',
           'Flat', 'Fort Hood', 'Fort Mc Kavett', 'Fulshear', 'Friendswood', 'Fred', 'Flynn', 'Fannin', 'Francitas',
           'Floresville', 'Falfurrias', 'Freer', 'Falcon Heights', 'Fentress', 'Fischer', 'Flatonia', 'Farnsworth',
           'Follett', 'Friona', 'Fritch', 'Flomot', 'Floydada', 'Fieldton', 'Fluvanna', 'Forsan', 'Fort Stockton',
           'Fabens', 'Fort Hancock', 'Fort Bliss', 'Firestone', 'Fort Collins', 'Fort Lupton', 'Fort Morgan', 'Flagler',
           'Fort Lyon', 'Fort Garland', 'Fruita', 'Fe Warren AFB', 'Fort Laramie', 'Frannie', 'Fort Washakie',
           'Four Corners', 'Farson', 'Fort Bridger', 'Fort Hall', 'Fish Haven', 'Filer', 'Fenn', 'Fort Duchesne',
           'Fielding', 'Ferron', 'Fountain Green', 'Fort Mcdowell', 'Fountain Hills', 'Fort Huachuca', 'Fort Apache',
           'Forest Lakes', 'Flagstaff', 'Fort Mohave', 'Fence Lake', 'Fort Wingate', 'Flora Vista', 'Fairacres',
           'Faywood', 'Fort Bayard', 'Fort Sumner', 'Fort Stanton', 'Fernley', 'Fallbrook', 'Fort Irwin', 'Fawnskin',
           'Forest Falls', 'Foothill Ranch', 'Fountain Valley', 'Fellows', 'Frazier Park', 'Firebaugh', 'Fish Camp',
           'Friant', 'Forest Knolls', 'Fields Landing', 'Fort Dick', 'Fiddletown', 'Foresthill', 'Feather Falls',
           'Forbestown', 'Forest Ranch', 'Fall River Mills', 'Flournoy', 'Forks Of Salmon', 'Fort Jones',
           'French Gulch', 'Floriston', 'Fort Bidwell', 'Fort Shafter', 'Fort Klamath', 'Fields', 'Fort Rock',
           'Frenchglen', 'Fossil', 'Federal Way', 'Fall City', 'Friday Harbor',
           'Forks', 'Fox Island', 'Fairchild Air Force Base', 'Four Lakes', 'False Pass', 'Fort Wainwright',
           'Fort Greely', 'Fort Yukon']
GCities = ['Garrochales', 'Guanica', 'Guayanilla', 'Gurabo', 'Guayama', 'GPO', 'Guaynabo', 'Gilbertville', 'Goshen',
           'Granby', 'Granville',
           'Glendale', 'Great Barrington', 'Greenfield', 'Gill', 'Gardner', 'Groton', 'Grafton', 'Georgetown',
           'Groveland', 'Gloucester', 'Greenbush', 'Green Harbor', 'Greene', 'Greenville', 'Goffstown', 'Gilmanton',
           'Glencliff', 'Gilford', 'Gilsum', 'Gorham', 'Groveton', 'Georges Mills', 'Grantham', 'Guild',
           'Gilmanton Iron Works', 'Glen', 'Greenland', 'Gray', 'Greenwood', 'Gardiner', 'Greenville Junction',
           'Guilford', 'Gouldsboro', 'Grand Lake Stream', 'Grand Isle', 'Glen Cove', 'Garland', 'Graniteville',
           'Gaysville', 'Glover', 'Greensboro', 'Greensboro Bend', 'Gilman', 'Guildhall', 'Glastonbury',
           'Grosvenor Dale', 'Gales Ferry', 'Gaylordsville', 'Greenwich', 'Greens Farms', 'GECC', 'Garfield', 'Garwood',
           'Glen Ridge', 'Glenwood', 'Glen Rock', 'Glasser', 'Great Meadows', 'Greendell', 'Gillette', 'Gladstone',
           'Green Village', 'Gibbsboro', 'Gibbstown', 'Glassboro', 'Glendora', 'Gloucester City', 'Grenloch',
           'Green Creek', 'Glen Gardner', 'Garrison', 'Goldens Bridge', 'Granite Springs', 'Garnerville',
           'Greenwood Lake', 'Grand View-On-Hudson', 'Glen Oaks', 'Great Neck', 'Garden City', 'Glen Head',
           'Glenwood Landing', 'Greenvale', 'Great River', 'Greenlawn', 'Greenport', 'Gallupville', 'Galway', 'Ghent',
           'Gilboa', 'Glenmont', 'Gloversville', 'Guilderland', 'Guilderland Center', 'Glasco', 'Glenford',
           'Grand Gorge', 'Greenfield Park', 'Germantown', 'Glenham', 'Glen Spey', 'Glen Wild', 'Grahamsville',
           'Glens Falls', 'Gansevoort', 'Greenfield Center', 'Gabriels', 'Genoa', 'Garrattsville', 'Glenfield', 'Greig',
           'Gouverneur', 'Great Bend', 'Gilbertsville', 'Glen Aubrey', 'Gainesville', 'Gasport', 'Getzville', 'Gowanda',
           'Grand Island', 'Geneseo', 'Geneva', 'Gerry', 'Great Valley', 'Greenhurst', 'Gibsonia', 'Glassport',
           'Greenock', 'Glenshaw', 'Garards Fort', 'Gastonville', 'Graysville', 'Gans', 'Gibbon Glade', 'Grindstone',
           'Garrett', 'Greensburg', 'Grapeville', 'Gipsy', 'Glen Campbell', 'Grove City', 'Guys Mills', 'Girard',
           'Grand Valley', 'Gallitzin', 'Glasgow', 'Glen Hope', 'Gifford', 'Glen Richey', 'Grampian', 'Grassflat',
           'Gaines', 'Galeton', 'Genesee', 'Gillett', 'Granville Summit', 'Grantville', 'Gratz', 'Greencastle',
           'Gardners', 'Gettysburg', 'Glenville', 'Gap', 'Goodville', 'Gordonville', 'Grover', 'Gilberton',
           'Girardville', 'Gordon', 'Germansville', 'Green Lane', 'Gilbert', 'Greeley', 'Greentown', 'Glen Lyon',
           'Gibson', 'Gardenville', 'Gladwyne', 'Glenolden', 'Glen Riddle Lima', 'Glenside', 'Gradyville',
           'Garnet Valley', 'Glen Mills', 'Glenmoore', 'Gwynedd', 'Gwynedd Valley', 'Geigertown', 'Great Mills',
           'Galesville', 'Greenbelt', 'Glenn Dale', 'Glen Echo', 'Gaithersburg', 'Garrett Park', 'Gunpowder',
           'Gambrills', 'Gibson Island', 'Glen Arm', 'Glen Burnie', 'Glyndon', 'Gwynn Oak', 'Grantsville', 'Galena',
           'Goldsboro', 'Grasonville', 'Glenelg', 'Girdletree', 'Great Falls', 'Greenway', 'Garrisonville', 'Gore',
           'Goldvein', 'Gordonsville', 'Glen Allen', 'Gloucester Point', 'Goochland', 'Grimstead', 'Gum Spring',
           'Gwynn', 'Greenbackville', 'Gasburg', 'Green Bay', 'Glade Hill', 'Glen Lyn', 'Goodview', 'Gate City',
           'Galax', 'Glade Spring', 'Glen Wilton', 'Grottoes', 'Gladys', 'Goode', 'Gretna', 'Grundy', 'Gary',
           'Gap Mills', 'Grassy Meadows', 'Green Bank', 'Gallagher', 'Gauley Bridge', 'Glen Ferris', 'Gandeeville',
           'Gay', 'Given', 'Gerrardstown', 'Glengary', 'Great Cacapon', 'Gallipolis Ferry', 'Griffithsville',
           'Glen Daniel', 'Glen Fork', 'Glen Jean', 'Glen Rogers', 'Glen White', 'Green Sulphur Springs', 'Glen Dale',
           'Glen Easton', 'Glady', 'Galloway', 'Gypsy', 'Grant Town', 'Gassaway', 'Gormania', 'Green Spring',
           'Germanton', 'Gibsonville', 'Goldston', 'Graham', 'Gulf', 'Garner', 'Garysburg', 'Gaston', 'Grimesland',
           'Gates', 'Gatesville', 'Grandy', 'Gastonia', 'Gold Hill', 'Granite Quarry', 'GMAC', 'Godwin', 'Grantsboro',
           'Grifton', 'Glade Valley', 'Glen Alpine', 'Glendale Springs', 'Granite Falls', 'Grassy Creek', 'Gerton',
           'Green Mountain', 'Gable', 'Gadsden', 'Greeleyville', 'Gaffney', 'Gramling', 'Goose Creek', 'Green Pond',
           'Galivants Ferry', 'Green Sea', 'Gresham', 'Gray Court', 'Greer', 'Gloverville', 'Garnett', 'Grayson',
           'Glenn', 'Griffin', 'Glennville', 'Gillsville', 'Good Hope', 'Gough', 'Gracewood', 'Grovetown', 'Guyton',
           'Glen Saint Mary', 'Green Cove Springs', 'Grandin', 'Graceville', 'Grand Ridge', 'Gonzalez', 'Gulf Breeze',
           'Gulf Hammock', 'Goldenrod', 'Grant', 'Greenacres', 'Gibsonton', 'Goodland', 'Gotha', 'Gardendale',
           'Goodwater', 'Gordo', 'Goodsprings', 'Guin', 'Gurley', 'Gallant', 'Gaylesville', 'Geraldine', 'Groveoak',
           'Guntersville', 'Georgiana', 'Grady', 'Gantt', 'Goodway', 'Grove Hill', 'Gainestown', 'Grand Bay',
           'Gulf Shores', 'Gallion', 'Gilbertown', 'Gallatin', 'Goodlettsville', 'Gladeville', 'Greenbrier',
           'Grandview', 'Gruetli Laager', 'Gatlinburg', 'Greenback', 'Greeneville', 'Gallaway', 'Grand Junction',
           'Gleason', 'Guys', 'Goodspring', 'Gainesboro', 'Grimsley', 'Glen Allan', 'Grace', 'Gunnison', 'Gattman',
           'Golden', 'Greenwood Springs', 'Guntown', 'Grenada', 'Gore Springs', 'Gallman', 'Goodman', 'Gulfport',
           'Gautier', 'Gloster', 'Glenview', 'Guston', 'Gravel Switch', 'Gray Hawk', 'Grays Knob', 'Gulston', 'Garrard',
           'Girdler', 'Goose Rock', 'Green Road', 'Glencoe', 'Grahn', 'Greenup', 'Grethel', 'Gunlock', 'Gays Creek',
           'Grand Rivers', 'Gamaliel', 'Gracey', 'Guthrie', 'Glens Fork', 'Gambier', 'Groveport', 'Green Camp',
           'Gibsonburg', 'Graytown', 'Gypsum', 'Grand Rapids', 'Grelton', 'Gratiot', 'Gates Mills', 'Grand River',
           'Garrettsville', 'Green', 'Greenford', 'Gnadenhutten', 'Galion', 'Green Springs', 'Gratis', 'Gallipolis',
           'Glouster', 'Guysville', 'Gomer', 'Glandorf', 'Grover Hill', 'Goldsmith', 'Gwynneville', 'Griffith',
           'Granger', 'Grovertown', 'Grabill', 'Galveston', 'Gas City', 'Grass Creek', 'Grissom Arb', 'Grantsburg',
           'Grammer', 'Greens Fork', 'Gosport', 'Gentryville', 'Goodells', 'Gregory', 'Grosse Ile', 'Grosse Pointe',
           'Goodrich', 'Grand Blanc', 'Gladwin', 'Gagetown', 'Glennie', 'Grand Ledge', 'Galesburg', 'Gobles', 'Galien',
           'Grass Lake', 'Gowen', 'Grand Haven', 'Grandville', 'GR', 'Glen Arbor', 'Grawn', 'Gaylord', 'Goetzville',
           'Good Hart', 'Grayling', 'Garden', 'Germfask', 'Gould City', 'Grand Marais', 'Gulliver', 'Gwinn', 'Gaastra',
           'Galt', 'Garden Grove', 'Grimes', 'Grinnell', 'Guthrie Center', 'Goodell', 'Gilmore City', 'Goldfield',
           'Gowrie', 'Garwin', 'Gladbrook', 'Grundy Center', 'Gravity', 'Galva', 'George', 'Gillett Grove',
           'Graettinger', 'Glidden', 'Griswold', 'Garber', 'Garnavillo', 'Guttenberg', 'Guernsey', 'Goose Lake',
           'Grand Mound', 'Glenbeulah', 'Genesee Depot', 'Genoa City', 'Greendale', 'Gotham', 'Glen Haven',
           'Grand Marsh', 'Glenwood City', 'Greenleaf', 'Green Valley', 'Granton', 'Gile', 'Glen Flora', 'Gays Mills',
           'Grand View', 'Green Lake', 'Goodhue', 'Grasston', 'Gibbon', 'Green Isle', 'Grand Portage', 'Grand Meadow',
           'Good Thunder', 'Granada', 'Garvin', 'Greenwald', 'Grey Eagle', 'Gonvick', 'Gully', 'Gatzke', 'Goodridge',
           'Grygla', 'Garretson', 'Gayville', 'Goodwin', 'Grenville', 'Gann Valley', 'Geddes', 'Glencross', 'Gwinner',
           'Grand Forks', 'Grand Forks AFB', 'GFAFB', 'Gilby', 'Glasston', 'Gackle', 'Grace City', 'Golden Valley',
           'Glen Ullin', 'Golva', 'Grassy Butte', 'Glenburn', 'Grenora', 'Garryowen', 'Grass Range', 'Greycliff',
           'Glentana', 'Glendive', 'Galata', 'Geyser', 'Gildford', 'Gallatin Gateway', 'Gold Creek', 'Grantsdale',
           'Golf', 'Grayslake', 'Gurnee', 'Great Lakes', 'Gilberts', 'Glen Ellyn', 'Glendale Heights', 'Gibson City',
           'Goodwine', 'Grant Park', 'Garden Prairie', 'German Valley', 'Gerlaw', 'Gilson', 'Glasford', 'Goodfield',
           'Graymont', 'Gridley', 'Gays', 'Gillespie', 'Glen Carbon', 'Godfrey', 'Golden Eagle', 'Granite City',
           'Griggsville', 'Glenarm', 'Greenview', 'Geff', 'Golden Gate', 'Grayville', 'Galatia', 'Golconda',
           'Goreville', 'Grand Chain', 'Grand Tower', 'Gerald', 'Gray Summit', 'Grubville', 'Gibbs', 'Gorin',
           'Green Castle', 'Green City', 'Greentop', 'Glenallen', 'Gideon', 'Gobler', 'Grayridge', 'Gatewood',
           'Grain Valley', 'Gentry', 'Gower', 'Grant City', 'Gilman City', 'Golden City', 'Gasconade', 'Gravois Mills',
           'Gilliam', 'Green Ridge', 'Graff', 'Grovespring', 'Goff', 'Gas', 'Garden Plain', 'Geuda Springs', 'Goddard',
           'Goessel', 'Grenola', 'Glen Elder', 'Glade', 'Gem', 'Gove', 'Grainfield', 'Gilead', 'Goehner', 'Giltner',
           'Glenvil', 'Guide Rock', 'Gothenburg', 'Gering', 'Garyville', 'Gramercy', 'Galliano', 'Gheens',
           'Golden Meadow', 'Grand Coteau', 'Gueydan', 'Grand Chenier', 'Gonzales', 'Geismar', 'Glynn',
           'Greenwell Springs', 'Grosse Tete', 'GMF', 'Gibsland', 'Goldonna', 'Grand Cane', 'Grambling', 'Glenmora',
           'Gorum', 'Gould', 'Gurdon', 'Garland City', 'Gillham', 'Grannis', 'Grapevine', 'Griffithville', 'Guy',
           'Gosnell', 'Gilmore', 'Grubbs', 'Gepp', 'Guion', 'Gassville', 'Green Forest', 'Gateway', 'Gravette',
           'Gravelly', 'Geary', 'Gotebo', 'Gracemont', 'Gene Autry', 'Geronimo', 'Grandfield', 'Granite', 'Goltry',
           'Gage', 'Gate', 'Goodwell', 'Guymon', 'Glenpool', 'Grove', 'Grand Prairie', 'Gunter', 'Grand Saline', 'GTE',
           'Gober', 'Gilmer', 'Gladewater', 'Grapeland', 'Glen Rose', 'Godley', 'Granbury', 'Goree', 'Graford',
           'Gorman', 'Gustine', 'Groesbeck', 'Goldthwaite', 'Gouldbusk', 'Goodfellow AFB', 'Galena Park', 'Gilchrist',
           'Groves', 'Gause', 'Ganado', 'Goliad', 'George West', 'Guerra', 'Garciasville', 'Grulla', 'Giddings',
           'Groom', 'Gruver', 'Gail', 'Girvin', 'Grandfalls', 'Grand Lake', 'Gilcrest', 'Green Mountain Falls',
           'Guffey', 'Glade Park', 'Glenwood Springs', 'Granite Canon', 'Glendo', 'Greybull', 'Glenrock', 'Green River',
           'Gooding', 'Gibbonsville', 'Grangeville', 'Greencreek', 'Garden Valley', 'Glenns Ferry', 'Grouse Creek',
           'Gold Canyon', 'Gila Bend', 'Goodyear', 'Globe', 'Gray Mountain', 'Grand Canyon', 'Gallina', 'Grants',
           'Gallup', 'Gamerco', 'Glorieta', 'Guadalupita', 'Gila', 'Garita', 'Gabbs', 'Gardnerville', 'Gerlach',
           'Glenbrook', 'Gardena', 'Granada Hills', 'Guasti', 'Guatay', 'Grand Terrace', 'Green Valley Lake', 'Goleta',
           'Grover Beach', 'Guadalupe', 'Greenbrae', 'Gilroy', 'Geyserville', 'Glen Ellen', 'Glenhaven', 'Graton',
           'Gualala', 'Guerneville', 'Garberville', 'Gasquet', 'Grizzly Flats', 'Guinda', 'Gold Run', 'Granite Bay',
           'Goodyears Bar', 'Grass Valley', 'Gazelle', 'Gerber', 'Gervais', 'Government Camp', 'Gales Creek',
           'Garibaldi', 'Grand Ronde', 'Gleneden Beach', 'Glide', 'Gold Beach', 'Grants Pass', 'Gold Bar', 'Greenbank',
           'Gig Harbor', 'Glenoma', 'Galvin', 'Grapeview', 'Grayland',
           'Goldendale', 'Grays River', 'Grand Coulee', 'Gakona', 'Girdwood', 'Glennallen', 'Goodnews Bay', 'Gambell',
           'Gustavus']
HCities = ['Holtsville', 'Hatillo', 'Hormigueros', 'Humacao', 'Hadley', 'Hampden', 'Hardwick', 'Hatfield',
           'Haydenville', 'Holyoke',
           'Huntington', 'Hinsdale', 'Housatonic', 'Heath', 'Harvard', 'Hubbardston', 'Holden', 'Holland',
           'Hanscom AFB', 'Holliston', 'Hopedale', 'Hopkinton', 'Hudson', 'Haverhill', 'Hamilton', 'Hathorne',
           'Hingham', 'Hull', 'Humarock', 'Hyde Park', 'Halifax', 'Hanover', 'Hanson', 'Holbrook', 'Hyannis', 'Harwich',
           'Harwich Port', 'Hyannis Port', 'Harmony', 'Harrisville', 'Hope', 'Hope Valley', 'Hollis', 'Hooksett',
           'Hebron', 'Henniker', 'Hill', 'Hillsborough', 'Holderness', 'Hancock', 'Hampstead', 'Hampton',
           'Hampton Falls', 'Harrison', 'Hiram', 'Hollis Center', 'Harpswell', 'Hallowell', 'Howland', 'Harborside',
           'Harrington', 'Hulls Cove', 'Houlton', 'Hartland', 'Hinckley', 'Hartford', 'Hartland Four Corners',
           'Highgate Center', 'Highgate Springs', 'Hinesburg', 'Hydeville', 'Haddam', 'Hadlyme', 'Hawleyville',
           'Higganum', 'Hamden', 'Harwinton', 'Hoboken', 'Hillside', 'Hamburg', 'Haskell', 'Hewitt', 'Highland Lakes',
           'Ho Ho Kus', 'Hawthorne', 'Haledon', 'Hackensack', 'Hasbrouck Heights', 'Harrington Park', 'Haworth',
           'Hillsdale', 'Hazlet', 'Howell', 'Highlands', 'Holmdel', 'Hackettstown', 'Hibernia', 'Hopatcong',
           'Haddonfield', 'Haddon Heights', 'Hainesport', 'Hammonton', 'Hancocks Bridge', 'Harrisonville',
           'Haddon Township', 'Heislerville', 'Hightstown', 'Hopewell', 'Helmetta', 'High Bridge', 'Highland Park',
           'Hartsdale', 'Hastings On Hudson', 'Harriman', 'Haverstraw', 'Highland Falls', 'Highland Mills', 'Hillburn',
           'Howells', 'Howard Beach', 'Hempstead', 'Hewlett', 'Huntington Station', 'Hauppauge', 'Hicksville',
           'Hampton Bays', 'Hagaman', 'Hannacroix', 'Hoosick', 'Hoosick Falls', 'Howes Cave', 'Haines Falls',
           'Halcottsville', 'Hensonville', 'High Falls', 'Highmount', 'Hunter', 'Hurley', 'Highland', 'Hollowville',
           'Holmes', 'Hopewell Junction', 'Hughsonville', 'Hankins', 'Harris', 'Highland Lake', 'Hortonville',
           'Huguenot', 'Hurleyville', 'Hague', 'Hudson Falls', 'Huletts Landing', 'Hannibal', 'Hastings', 'Homer',
           'Hartwick', 'Herkimer', 'Hoffmeister', 'Holland Patent', 'Hubbardsville', 'Hailesboro', 'Hammond',
           'Hannawa Falls', 'Helena', 'Henderson', 'Henderson Harbor', 'Hermon', 'Heuvelton', 'Hogansburg', 'Harford',
           'Harpersfield', 'Harpursville', 'Hobart', 'Hall', 'Hamlin', 'Hemlock', 'Henrietta', 'Hilton', 'Holley',
           'Honeoye', 'Honeoye Falls', 'Houghton', 'Hume', 'Hammondsport', 'Hector', 'Himrod', 'Hornell', 'Horseheads',
           'Hunt', 'Harwick', 'Hookstown', 'Homestead', 'Hendersonville', 'Hickory', 'Houston', 'Hibbs', 'Hiller',
           'Hopwood', 'Hidden Valley', 'Hyndman', 'Hannastown', 'Harrison City', 'Herminie', 'Hostetter', 'Hunker',
           'Hutchinson', 'Heilwood', 'Home', 'Homer City', 'Hollsopple', 'Hooversville', 'Herman', 'Hilliards',
           'Hartstown', 'Hillsville', 'Hermitage', 'Hawthorn', 'Hydetown', 'Harborcreek', 'Harmonsburg', 'Hesston',
           'Hollidaysburg', 'Houtzdale', 'Huntingdon', 'Hazel Hurst', 'Hawk Run', 'Howard', 'Hyde', 'Harrison Valley',
           'Hershey', 'Highspire', 'Honey Grove', 'Hummelstown', 'Harrisburg', 'Hustontown', 'Holtwood', 'Hopeland',
           'Hughesville', 'Hartleton', 'Herndon', 'Hummels Wharf', 'Hegins', 'Hellertown', 'Hereford', 'Hazleton',
           'Harleigh', 'Henryville', 'Hawley', 'Herrick Center', 'Honesdale', 'Harveys Lake', 'Hillsgrove',
           'Hunlock Creek', 'Huntington Mills', 'Hallstead', 'Hop Bottom', 'Hilltown', 'Holicong', 'Huntingdon Valley',
           'Hatboro', 'Haverford', 'Horsham', 'Havertown', 'Honey Brook', 'Harleysville', 'Hockessin', 'Harbeson',
           'Hartly', 'Haymarket', 'Helen', 'Hollywood', 'Huntingtown', 'Harwood', 'Hyattsville', 'HHS', 'Hunt Valley',
           'Harmans', 'Havre De Grace', 'Hydes', 'Halethorpe', 'Hillsboro', 'Hurlock', 'Hagerstown', 'Hartwood',
           'Haynesville', 'Heathsville', 'Hustle', 'Huntly', 'Haywood', 'Hood', 'Harrisonburg', 'Hinton', 'Hadensville',
           'Hallieford', 'Hardyville', 'Hartfield', 'Hayes', 'Henrico', 'Hudgins', 'Hacksneck', 'Hallwood', 'Harborton',
           'Horntown', 'Hampden Sydney', 'Hardy', 'Henry', 'Huddleston', 'Haysi', 'Hiltons', 'Honaker', 'Hiwassee',
           'Head Waters', 'Hot Springs', 'Howardsville', 'Hurt', 'Horsepen', 'Hiawatha', 'Hensley', 'Handley',
           'Hansford', 'Hernshaw', 'Hewett', 'Hometown', 'Hugheston', 'Halltown', 'Harpers Ferry', 'Hedgesville',
           'Harts', 'Hurricane', 'Henlawson', 'Harper', 'Hico', 'Hilltop', 'Hacker Valley', 'Helvetia', 'Hambleton',
           'Harman', 'Hendricks', 'Huttonsville', 'Hepzibah', 'Horner', 'Hundred', 'Heaters', 'High View',
           'Hamptonville', 'Haw River', 'Highfalls', 'High Point', 'H P', 'Holly Springs', 'Hurdle Mills', 'Hassell',
           'Hobgood', 'Hollister', 'Harbinger', 'Harrellsville', 'Hatteras', 'Hertford', 'Hobbsville', 'Huntersville',
           'High Shoals', 'Hamlet', 'Hoffman', 'Hope Mills', 'Hallsboro', 'Harrells', 'Holly Ridge', 'Harkers Island',
           'Havelock', 'Hobucken', 'Hookerton', 'Hubert', 'Hays', 'Hiddenite', 'Hildebran', 'Hazelwood', 'Horse Shoe',
           'Hayesville', 'Heath Springs', 'Holly Hill', 'Hopkins', 'Horatio', 'Hanahan', 'Harleyville', 'Huger',
           'Hamer', 'Hartsville', 'Hemingway', 'Hodges', 'Honea Path', 'Hickory Grove', 'Hilda', 'Hilton Head Island',
           'Hardeeville', 'Haralson', 'Hogansville', 'Hagan', 'Hiawassee', 'Hoschton', 'Hartwell', 'Harlem',
           'Hephzibah', 'Haddock', 'Hawkinsville', 'Hinesville', 'Hazlehurst', 'Hortense', 'Hahira', 'Homerville',
           'Hartsfield', 'Hilliard', 'Havana', 'Hosford', 'Hurlburt Field', 'Holt', 'High Springs', 'Horseshoe Beach',
           'HBJ', 'Hialeah', 'Hallandale', 'Hobe Sound', 'Haines City', 'Highland City', 'Homeland', 'Holmes Beach',
           'Hernando', 'Holder', 'Homosassa', 'Homosassa Springs', 'Holiday', 'Howey In The Hills', 'Hanceville',
           'Harpersville', 'Hayden', 'Hollins', 'Holly Pond', 'Hackleburg', 'Haleyville', 'Hartselle', 'Harvest',
           'Hazel Green', 'Hollytree', 'Huntsville', 'Henagar', 'Higdon', 'Horton', 'Hardaway', 'Hayneville',
           'Highland Home', 'Honoraville', 'Hope Hull', 'Heflin', 'Headland', 'Huxford', 'Hatchechubbee',
           'Holy Trinity', 'Hurtsboro', 'Hurricane Mills', 'Hixson', 'Huntland', 'Harrogate', 'Heiskell', 'Helenwood',
           'Halls', 'Henning', 'Hickory Valley', 'Hornsby', 'Hornbeak', 'Holladay', 'Hollow Rock', 'Humboldt', 'Huron',
           'Hampshire', 'Hohenwald', 'Hickman', 'Hilham', 'Hickory Flat', 'Horn Lake', 'Hollandale', 'Houlka',
           'Holcomb', 'Harperville', 'Harriston', 'Hermanville', 'Holly Bluff', 'Hattiesburg', 'Heidelberg',
           'Harrods Creek', 'Hillview', 'Hardinsburg', 'Harned', 'Harrodsburg', 'Hustonville', 'Harlan', 'Helton',
           'Holmes Mill', 'Hoskinston', 'Hulen', 'Heidrick', 'Hima', 'Hinkle', 'Hitchins', 'Hagerhill', 'Hellier',
           'Huddy', 'Harold', 'Hi Hat', 'Hueysville', 'Hazard', 'Happy', 'Hyden', 'Hallie', 'Hindman', 'Hardin',
           'Hazel', 'Hestand', 'Hiseville', 'Hopkinsville', 'Hawesville', 'Horse Branch', 'Hodgenville', 'Horse Cave',
           'Hideaway Hls', 'Harpster', 'Harbor View', 'Hamler', 'Haskins', 'Holgate', 'Hoytville', 'Hammondsville',
           'Holloway', 'Huntsburg', 'Hanoverton', 'Hubbard', 'Hartville', 'Holmesville', 'Homeworth', 'Harveysburg',
           'Hooven', 'Hamersville', 'Higginsport', 'Hollansburg', 'Hallsville', 'Hockingport', 'Harrod', 'Haviland',
           'Hobbs', 'Hanna', 'Hoagland', 'Howe', 'Huntertown', 'Holton', 'Hartford City', 'Helmsburg', 'Heltonville',
           'Huntingburg', 'Haubstadt', 'Hymera', 'Harsens Island', 'Hazel Park', 'Harrison Township',
           'Huntington Woods', 'Hamtramck', 'Harper Woods', 'Harbor Beach', 'Holly', 'Higgins Lake', 'Houghton Lake',
           'Houghton Lake Heights', 'Hale', 'Haslett', 'Hagar Shores', 'Hickory Corners', 'Harbert', 'Howard City',
           'Hart', 'Hesperia', 'Hudsonville', 'Harrietta', 'Hersey', 'Honor', 'Harbor Springs', 'Hawks', 'Herron',
           'Hessel', 'Hillman', 'Hubbard Lake', 'Hulbert', 'Hermansville', 'Hubbell', 'Harvey', 'Humeston', 'Huxley',
           'HP', 'Hanlontown', 'Harcourt', 'HP-SC/YE', 'Hawarden', 'Holstein', 'Hornick', 'Hospers', 'Hartley',
           'Halbur', 'Honey Creek', 'Holy Cross', 'Hawkeye', 'Highlandville', 'Hills', 'Hedrick', 'Horicon', 'Hubertus',
           'Hustisford', 'Hales Corners', 'Helenville', 'Hillpoint', 'Hager City', 'Hilbert', 'Hatley', 'Harshaw',
           'Hawkins', 'Hazelhurst', 'Heafford Junction', 'Hixton', 'Holmen', 'Hustler', 'Holcombe', 'Humbird', 'Haugen',
           'Hayward', 'Herbster', 'Hertel', 'Henriette', 'Hugo', 'Hamel', 'Howard Lake', 'Hovland', 'Hibbing',
           'Hill City', 'Hoyt Lakes', 'Hayfield', 'Hokah', 'Hanska', 'Huntley', 'Heron Lake', 'Hanley Falls',
           'Holdingford', 'Holmes City', 'Halstad', 'Hendrum', 'Hitterdal', 'Hines', 'Hallock', 'Halma', 'Hayti',
           'Highmore', 'Hitchcock', 'Hecla', 'Hosmer', 'Hoven', 'Hamill', 'Harrold', 'Herrick', 'Holabird', 'Herreid',
           'Hermosa', 'Howes', 'Hankinson', 'Horace', 'Hannah', 'Hatton', 'Hensel', 'Hoople', 'Hansboro', 'Hannaford',
           'Hurdsfield', 'Hazelton', 'Hazen', 'Halliday', 'Hettinger', 'Harlowton', 'Hysham', 'Hathaway', 'Heart Butte',
           'Highwood', 'Hilger', 'Hobson', 'Havre', 'Hogeland', 'Haugan', 'Helmville', 'Heron', 'Huson', 'Hungry Horse',
           'Hanover Park', 'Hoffman Estates', 'Hazel Crest', 'Homewood', 'Hickory Hills', 'Homer Glen',
           'Harwood Heights', 'Herscher', 'Hoopeston', 'Hopkins Park', 'Harmon', 'Hooppole', 'Hennepin', 'Hanna City',
           'Heyworth', 'Hindsboro', 'Hagarstown', 'Hecker', 'Huey', 'Hidalgo', 'Hutsonville', 'Harristown', 'Harvel',
           'Hartsburg', 'Hettick', 'Hoyleton', 'Herod', 'Herrin', 'Hurst', 'Hematite', 'Herculaneum', 'High Ridge',
           'House Springs', 'Hawk Point', 'High Hill', 'Hunnewell', 'Hurdland', 'Hornersville', 'Harviell',
           'Higginsville', 'Humphreys', 'Henley', 'Hermann', 'Holts Summit', 'Higbee', 'Holliday', 'Houstonia',
           'Hartshorn', 'Huggins', 'Half Way', 'Hardenville', 'Humansville', 'Harveyville', 'Havensville', 'Hoyt',
           'Hepler', 'Hollenberg', 'Halstead', 'Hardtner', 'Haysville', 'Herington', 'Holyrood', 'Haven', 'Hoisington',
           'Hoxie', 'Hanston', 'Healy', 'Hugoton', 'Hooper', 'Hallam', 'Humphrey', 'Hadar', 'Hartington', 'Hoskins',
           'Hordville', 'Heartwell', 'Hendley', 'Hildreth', 'Holdrege', 'Haigler', 'Hayes Center', 'Halsey',
           'Hay Springs', 'Hemingford', 'Hahnville', 'Houma', 'Husser', 'Hackberry', 'Hester', 'Hall Summit',
           'Haughton', 'Hosston', 'Hodge', 'Hessmer', 'Hineston', 'Hornbeck', 'Harrell', 'Huttig',
           'Hot Springs National Park', 'HS', 'Hot Springs Village', 'Hattieville', 'Hickory Plains', 'Higden',
           'Higginson', 'Holly Grove', 'Humnoke', 'Haynes', 'Heth', 'Hickory Ridge', 'Hughes', 'Horseshoe Bend',
           'Heber Springs', 'Harriet', 'Hasty', 'Hindsville', 'Hiwasse', 'Hagarville', 'Hartman', 'Hackett', 'Harrah',
           'Hydro', 'Healdton', 'Headrick', 'Hammon', 'Hennessey', 'Hopeton', 'Hardesty', 'Hooker', 'Hallett', 'Hominy',
           'Henryetta', 'Hitchita', 'Haileyville', 'Hartshorne', 'Hendrix', 'Holdenville', 'Heavener', 'Hodgen',
           'Hutchins', 'Hooks', 'Harleton', 'Hughes Springs', 'Hemphill', 'Haslet', 'Haltom City', 'Heidenheimer',
           'Harker Heights', 'Hext', 'Huffman', 'Hufsmith', 'Humble', 'Hockley', 'Hungerford', 'Hankamer', 'Hamshire',
           'High Island', 'Hillister', 'Hearne', 'Hallettsville', 'Hochheim', 'Helotes', 'Hebbronville', 'Hargill',
           'Harlingen', 'Hutto', 'Hye', 'Horseshoe Bay', 'Hondo', 'Hale Center', 'Higgins', 'Hedley', 'Hermleigh',
           'Hartsel', 'Hot Sulphur Springs', 'Hygiene', 'Haxtun', 'Hillrose', 'Haswell', 'Hoehne', 'Homelake',
           'Hesperus', 'Hotchkiss', 'Horse Creek', 'Hawk Springs', 'Hyattville', 'Hiland', 'Hulett', 'Hagerman',
           'Hailey', 'Hansen', 'Heyburn', 'Hammett', 'Homedale', 'Huston', 'Heber City', 'Henefer', 'Hill AFB',
           'Herriman', 'Honeyville', 'Hyrum', 'Helper', 'Hanksville', 'Hatch', 'Henrieville', 'Hildale', 'Higley',
           'Huachuca City', 'Heber', 'Happy Jack', 'Hotevilla', 'Hualapai', 'Houck', 'Hernandez', 'Holman', 'Hachita',
           'House', 'High Rolls Mountain Park', 'Holloman Air Force Base', 'Hiko', 'Hermosa Beach', 'Huntington Park',
           'Harbor City', 'Hawaiian Gardens', 'Hacienda Heights', 'Holtville', 'Helendale', 'Hinkley', 'Hemet',
           'Huntington Beach', 'Hanford', 'Helm', 'Half Moon Bay', 'Hercules', 'Holy City', 'Hathaway Pines', 'Hilmar',
           'Hornitos', 'Hughson', 'Healdsburg', 'Hopland', 'Hidden Valley Lake', 'Honeydew', 'Hoopa', 'Hydesville',
           'Herald', 'Hamilton City', 'Happy Camp', 'Hat Creek', 'Hayfork', 'Hornbrook', 'Hyampom', 'Herlong', 'Haiku',
           'Hakalau', 'Haleiwa', 'Hana', 'Hanalei', 'Hanamaulu', 'Hanapepe', 'Hauula', 'Hawaii National Park', 'Hawi',
           'Hilo', 'Holualoa', 'Honaunau', 'Honokaa', 'Honomu', 'Hoolehua', 'Honolulu', 'Hagatna', 'Hood River',
           'Happy Valley', 'Hebo', 'Haines', 'Halfway', 'Helix', 'Heppner', 'Hermiston', 'Hansville',
           'Hoodsport', 'Hoquiam', 'Humptulips', 'Heisson', 'Husum', 'Hartline', 'Hay', 'Hunters', 'Hooper Bay',
           'Huslia', 'Hoonah', 'Hydaburg', 'Hyder']
ICities = ['Isabela', 'Indian Orchard', 'Ipswich', 'Intervale', 'Isle Of Springs', 'Isle Au Haut', 'Islesford',
           'Island Falls', 'Islesboro', 'Isle La Motte', 'Irasburg', 'Island Pond', 'IRS', 'Ivoryton', 'Irvington',
           'Ironia', 'Imlaystown', 'Island Heights',
           'Iselin', 'Inwood', 'Island Park', 'Islandia', 'Islip', 'Islip Terrace', 'Indian Lake', 'Ilion', 'Inlet',
           'Irving', 'Ionia', 'Interlaken', 'Ithaca', 'Indianola', 'Industry', 'Imperial', 'Ingomar', 'Indian Head',
           'Isabella', 'Irwin', 'Indiana', 'Irvine', 'Imler',
           'Irvona', 'Ickesburg', 'Idaville', 'Intercourse', 'Immaculata', 'Ironsides', 'Issue', 'Ingleside',
           'Ijamsville', 'Ivy', 'Isle Of Wight', 'Ivor', 'Indian Valley', 'Independence', 'Ivanhoe', 'Iron Gate',
           'Iaeger', 'Ikes Fork', 'Isaban', 'Itmann', 'Indore', 'Institute', 'Ivydale', 'Ireland', 'Idamay',
           'Indian Trail', 'Iron Station', 'Icard', 'Irmo', 'Inman', 'Isle Of Palms', 'Iva', 'Islandton', 'Ila',
           'Ideal', 'Irwinton', 'Irwinville', 'Interlachen', 'Island Grove', 'Indialantic', 'Islamorada',
           'Indian Rocks Beach', 'Intercession City', 'Indian Lake Estates', 'Immokalee', 'Inglis', 'Inverness',
           'Istachatta', 'Indiantown', 'Ider', 'Indian Mound', 'Idlewild', 'Iron City', 'Isola', 'Iuka', 'Itta Bena',
           'Ingram', 'Isonville', 'Inez', 'Ivel', 'Isom', 'Island', 'Iberia', 'Isle Saint George', 'Irondale',
           'Ironton', 'Ingalls', 'Indianapolis', 'Inglefield', 'Ida', 'Inkster', 'Imlay City', 'Interlochen', 'Irons',
           'Indian River', 'Iron Mountain', 'Ishpeming', 'Iron River', 'Ironwood', 'Iowa Falls', 'Ira', 'Ireton',
           'Ida Grove', 'Imogene', 'Iowa City', 'Iron Ridge', 'Ixonia', 'Irma', 'Iron Belt', 'Iola', 'Isanti',
           'Inver Grove Heights', 'Iron', 'Ihlen', 'Iona', 'Isle', 'International Falls', 'Irene', 'Iroquois', 'Isabel',
           'Interior', 'Ismay', 'Island Lake', 'Itasca', 'Illinois City', 'Ipava', 'Ivesdale', 'Ingraham', 'Illiopolis',
           'Ina', 'Inavale', 'Inland', 'Iota', 'Iowa', 'Innis', 'Ivan', 'Imboden', 'Indiahoma', 'Inola', 'Idabel',
           'Iowa Park', 'Iredell', 'Italy', 'Idalou', 'Iraan', 'Idaho Springs', 'Idledale', 'Indian Hills', 'Idalia',
           'Iliff', 'Ignacio', 'Inkom', 'Idaho Falls', 'Idaho City', 'Ibapah', 'Ivins', 'Indian Wells', 'Isleta',
           'Ilfeld', 'Indian Springs', 'ISAFA', 'Imlay', 'Incline Village', 'Inglewood', 'Imperial Beach', 'Indio',
           'Idyllwild', 'Inyokern', 'I B M', 'Ione', 'Isleton', 'Igo', 'Inarajan',
           'Idanha', 'Idleyld Park', 'Imbler', 'Imnaha', 'Irrigon', 'Ironside', 'Issaquah', 'Index', 'Ilwaco',
           'Inchelium', 'Indian', 'Iliamna']
JCities = ['Jayuya', 'Juncos', 'Juana Diaz', 'Jefferson', 'Jamaica Plain', 'Jamestown', 'Johnston', 'Jaffrey',
           'Jackson', 'Jay', 'Jonesboro',
           'Jonesport', 'Jackman', 'Jacksonville', 'Jamaica', 'Jeffersonville', 'Jericho', 'Jonesville', 'Johnson',
           'Jewett City', 'Jersey City', 'Johnsonburg', 'Jobstown', 'Juliustown', 'Jefferson Valley', 'Jackson Heights',
           'Jamesport', 'Johnsonville', 'Johnstown', 'Jewett', 'Johnsburg', 'Jamesville', 'Jordan', 'Jordanville',
           'Johnson City', 'Java Center', 'Java Village', 'Jasper', 'Joffre', 'Jacobs Creek', 'Jenners', 'Jennerstown',
           'Jeannette', 'Jones Mills', 'Josephine', 'Jerome', 'Jackson Center', 'James Creek', 'James City', 'Julian',
           'Jonestown', 'Jersey Mills', 'Jersey Shore', 'Jim Thorpe', 'Junedale', 'Jermyn', 'Jessup', 'Jamison',
           'Jenkintown', 'Jarrettsville', 'Joppa', 'Jersey', 'Jeffersonton', 'Jetersville', 'Jenkins Bridge', 'Jarratt',
           'Java', 'Jewell Ridge', 'Jenkinjones', 'Jesse', 'Jolo', 'Justice', 'Jeffrey', 'Jumping Branch', 'Junior',
           'Jacksonburg', 'Jane Lew', 'Jackson Springs', 'Jarvisburg', 'Jonas Ridge', 'Jenkinsville', 'Joanna',
           'Jacksonboro', 'Johns Island', 'Jenkinsburg', 'Jewell', 'Juliette', 'Jekyll Island', 'Jesup',
           'Junction City', 'Jennings', 'Jacksonville Beach', 'Jupiter', 'JPV', 'Jensen Beach', 'Jemison', 'Jack',
           'Jones', 'Jacksons Gap', 'Jachin', 'Joelton', 'JC', 'Jonesborough', 'Jacksboro', 'Jefferson City', 'Jellico',
           'Jacks Creek', 'Jayess', 'Jakin', 'Jenkins', 'Jonancy', 'Jeff', 'Jackhorn', 'Jeremiah', 'Jetson',
           'Jacksontown', 'Jerry City', 'Jerusalem', 'Jacobsburg', 'Jeromesville', 'Jenera', 'Jasonville', 'Jeddo',
           'Jenison', 'Johannesburg', 'Joice', 'Jolley', 'Janesville', 'Johnson Creek', 'Juneau', 'Juda', 'Jump River',
           'Jim Falls', 'Jacobson', 'Jeffers', 'Jessie', 'Jud', 'Joliet', 'Judith Gap', 'Joplin', 'Joy', 'Jerseyville',
           'Jacob', 'Johnston City', 'Junction', 'Jonesburg', 'Jameson', 'Jerico Springs', 'Jadwin', 'Jetmore',
           'Jansen', 'Juniata', 'Jeanerette', 'Jarreau', 'Jigger', 'Jena', 'Joyce', 'Jessieville', 'Jacksonport',
           'Judsonia', 'Jones Mill', 'Joiner', 'Jet', 'Jenks', 'Joinerville', 'Judson', 'Joaquin', 'Joshua', 'Justin',
           'Jarrell', 'Jourdanton', 'Justiceburg', 'Jayton', 'Julesburg', 'Joes', 'Jaroso', 'Jelm', 'Jay Em',
           'Jeffrey City', 'Juliaetta', 'Jensen', 'Joseph', 'Joseph City', 'Jarales', 'Jemez Pueblo', 'Jemez Springs',
           'Jal', 'Jean', 'Jackpot', 'Jarbidge', 'Jacumba',
           'Jamul', 'Joshua Tree', 'June Lake', 'Jolon', 'Jenner', 'Jb Phh', 'John Day', 'Jamieson', 'Jordan Valley',
           'Juntura', 'JBLM', 'Jber']
KCities = ['Kingshill', 'Kingston', 'Kenyon', 'Keene', 'Kearsarge', 'Kittery', 'Kittery Point', 'Kennebunk',
           'Kennebunkport', 'Kents Hill',
           'Kenduskeag', 'Kingman', 'Kingfield', 'Killington', 'Killingworth', 'Kent', 'Kearny', 'Kenilworth',
           'Keansburg', 'Keyport', 'Kenvil', 'Kendall Park', 'Keasbey', 'Katonah', 'Kew Gardens', 'Kings Park',
           'Kinderhook', 'Knox', 'Kerhonkson', 'Kauneonga Lake', 'Kenoza Lake', 'Kiamesha Lake', 'Kattskill Bay',
           'Keeseville', 'Keene Valley', 'King Ferry', 'Kirkville', 'Knoxboro', 'Killawog', 'Kirkwood', 'Kendall',
           'Keuka Park', 'Knowlesville', 'Kennedy', 'Kill Buck', 'Kanona', 'Keisterville', 'Kantner', 'Kersey',
           'Knox Dale', 'Karns City', 'Koppel', 'Kittanning', 'Kossuth', 'Kennerdell', 'Kane', 'Karthaus', 'Kylertown',
           'Knoxville', 'Kleinfeltersville', 'Kinzers', 'Kreamer', 'Kulpmont', 'Klingerstown', 'Kunkletown', 'Kelayres',
           'Kresgeville', 'Kingsley', 'Kintnersville', 'Kelton', 'Kemblesville', 'Kennett Square', 'King Of Prussia',
           'Kimberton', 'Kulpsville', 'Kempton', 'Kutztown', 'Kenton', 'Kensington', 'Kingsville', 'Kitzmiller',
           'Kennedyville', 'Keedysville', 'Keymar', 'Kilmarnock', 'King George', 'Kinsale', 'Keezletown', 'Keswick',
           'Kents Store', 'King And Queen Court House', 'King William', 'Keller', 'Kenbridge', 'Keysville', 'Keokee',
           'Keeling', 'Keen Mountain', 'Kegley', 'Kellysville', 'Kimball', 'Kopperston', 'Kyle', 'Kanawha Falls',
           'Kimberly', 'Kincaid', 'Kenna', 'Kearneysville', 'Kenova', 'Kiahsville', 'Kistler', 'Kermit', 'Kanawha Head',
           'Kerens', 'Kingwood', 'Kingmont', 'Keslers Cross Lanes', 'Keyser', 'King', 'Kernersville', 'Kenly',
           'Kipling', 'Kittrell', 'Knightdale', 'Kelford', 'Kill Devil Hills', 'Kitty Hawk', 'Knotts Island',
           'Kannapolis', 'Kings Mountain', 'Kenansville', 'Kelly', 'Kure Beach', 'Kinston', 'Kershaw', 'Kinards',
           'Kingstree', 'Kennesaw', 'Kathleen', 'Kite', 'Kings Bay', 'Kingsland', 'Keystone Heights', 'Key Largo',
           'Key West', 'Key Colony Beach', 'Key Biscayne', 'Killarney', 'Kissimmee', 'Kellyton', 'Kellerman', 'Kansas',
           'Killen', 'Kingston Springs', 'Kelso', 'Kingsport', 'Kodak', 'Kyles Ford', 'Kosciusko', 'Kiln', 'Kokomo',
           'Kilmichael', 'Keavy', 'Kenvir', 'Kettle Island', 'Keaton', 'Kimper', 'Krypton', 'Kevil', 'Kirksey',
           'Kuttawa', 'Knob Lick', 'Knifley', 'Kilbourne', 'Kirkersville', 'Kirby', 'Kelleys Island', 'Kunkle',
           'Kimbolton', 'Kipton', 'Kinsman', 'Kidron', 'Killbuck', 'Kings Mills', 'Kettlersville', 'Kerr', 'Kitts Hill',
           'Kalida', 'Kirklin', 'Knightstown', 'Kingsbury', 'Kingsford Heights', 'Kouts', 'Kendallville', 'Keystone',
           'Kimmell', 'Kewanna', 'Kurtz', 'Kennard', 'Koleen', 'Knightsville', 'Kentland', 'Keego Harbor', 'Kinde',
           'Kawkawlin', 'Kalamazoo', 'Kent City', 'Kaleva', 'Kalkaska', 'Kewadin', 'Kinross', 'Kincheloe', 'Kingsford',
           'Kamrar', 'Kellerton', 'Kelley', 'Kellogg', 'Killduff', 'Kanawha', 'Kensett', 'Klemme', 'Knierim', 'Kesley',
           'Kirkman', 'Kiron', 'Kimballton', 'Kalona', 'Keota', 'Keosauqua', 'Keokuk', 'Kewaskum', 'Kiel', 'Kohler',
           'Kansasville', 'Kenosha', 'Kieler', 'Kaukauna', 'Keshena', 'Krakow', 'Kellnersville', 'Kewaunee', 'Kennan',
           'Knapp', 'Knife River', 'Keewatin', 'Kerrick', 'Kettle River', 'Kinney', 'Kasson', 'Kasota', 'Kiester',
           'Kilkenny', 'Kanaranzi', 'Kenneth', 'Kandiyohi', 'Kerkhoven', 'Kelliher', 'Kabetogama', 'Karlstad',
           'Kranzburg', 'Kaylor', 'Kadoka', 'Kennebec', 'Keldron', 'Kathryn', 'Kindred', 'Kensal', 'Kulm', 'Kintyre',
           'Killdeer', 'Karlsruhe', 'Kenmare', 'Kramer', 'Kinsey', 'Kevin', 'Kremlin', 'Kalispell', 'Kila', 'Kaneville',
           'Kirkland', 'Kankakee', 'Kasbeer', 'Keithsburg', 'Kewanee', 'Kingston Mines', 'Kenney', 'Kampsville',
           'Keyesport', 'Keenes', 'Keensburg', 'Kell', 'Kinmundy', 'Karbers Ridge', 'Karnak', 'Kimmswick', 'Kahoka',
           'Knox City', 'Kirksville', 'Kennett', 'Kearney', 'Kansas City', 'KC', 'King City', 'Kidder', 'Kaiser',
           'Koeltztown', 'Keytesville', 'Kingdom City', 'Knob Noster', 'Kirbyville', 'Kissee Mills', 'Kimberling City',
           'Koshkonong', 'Kechi', 'Kiowa', 'Kanopolis', 'Kinsley', 'Kirwin', 'Kanorado', 'Kismet', 'Kenesaw', 'Kilgore',
           'Kenner', 'Kraemer', 'Kentwood', 'Kaplan', 'Kinder', 'Krotz Springs', 'Keatchie', 'Keithville', 'Kurthwood',
           'Keo', 'Keiser', 'Knobel', 'Kingfisher', 'Keyes', 'Kellyville', 'Kiefer', 'Ketchum',
           'Kiamichi Christian Mission', 'Kinta', 'Krebs', 'Kaw City', 'Kemp', 'Kenefic', 'Konawa', 'Kaufman',
           'Klondike', 'Kildare', 'Karnack', 'Kirvin', 'Kennedale', 'Krum', 'Kamay', 'Kempner', 'Killeen', 'Kopperl',
           'Kosse', 'Knickerbocker', 'Katy', 'Kendleton', 'Kemah', 'Kountze', 'Kurten', 'Kendalia', 'Kerrville',
           'Karnes City', 'Kenedy', 'Knippa', 'Kress', 'Knott', 'Kittredge', 'Kremmling', 'Keenesburg', 'Karval',
           'Kirk', 'Kit Carson', 'Kim', 'Kinnear', 'Kaycee', 'Kemmerer', 'Kamiah', 'Kendrick', 'Kooskia', 'King Hill',
           'Kuna', 'Kootenai', 'Kamas', 'Kaysville', 'Kanosh', 'Kanab', 'Kanarraville', 'Koosharem', 'Kayenta',
           'Keams Canyon', 'Kykotsmovi Village', 'Kaibeto', 'Kirtland AFB', 'Kirtland', 'Kaweah', 'Kernville',
           'Kettleman City', 'Keeler', 'Kerman', 'Kingsburg', 'Kings Canyon National Pk', 'Knightsen', 'Kentfield',
           'Kelseyville', 'Kenwood', 'Klamath', 'Kneeland', 'Korbel', 'Knights Landing', 'Kyburz', 'Klamath River',
           'Kings Beach', 'Kapolei', 'Kaaawa', 'Kahuku', 'Kahului', 'Kailua', 'Keauhou', 'Kailua Kona', 'Kalaheo',
           'Kalaupapa', 'Kamuela', 'Kaneohe', 'Kapaa', 'Kaumakani', 'Kaunakakai', 'Keaau', 'Kealakekua', 'Kealia',
           'Kekaha', 'Kihei', 'Kilauea', 'Kapaau', 'Koloa', 'Kualapuu', 'Kunia', 'Kurtistown', 'Kula', 'Kosrae',
           'Keizer', 'Kerby', 'Klamath Falls', 'Keno', 'Kenmore', 'Kapowsin', 'Kalama', 'Klickitat', 'Kittitas',
           'Kettle Falls', 'Kahlotus', 'Kennewick', 'Kongiganak', 'Kalskag', 'Karluk', 'Kasigluk', 'Kasilof', 'Kenai',
           'King Cove', 'King Salmon', 'Kipnuk', 'Kodiak', 'Kotlik', 'Kwethluk',
           'Kwigillingok', 'Kaktovik', 'Kaltag', 'Kiana', 'Kivalina', 'Kobuk', 'Kotzebue', 'Koyuk', 'Koyukuk', 'Kake',
           'Ketchikan', 'Klawock']
LCities = ['Lajas', 'Lares', 'Las Marias', 'Las Piedras', 'Loiza', 'Luquillo', 'La Plata', 'Leeds', 'Leverett',
           'Ludlow', 'Longmeadow', 'Lanesboro', 'Lee',
           'Lenox', 'Lenox Dale', 'Lake Pleasant', 'Leominster', 'Littleton', 'Lunenburg', 'Lancaster', 'Leicester',
           'Linwood', 'Lincoln', 'Lawrence', 'Lowell', 'Lynn', 'Lynnfield', 'Lakeville', 'Lexington', 'Little Compton',
           'Litchfield', 'Londonderry', 'Lyndeborough', 'Laconia', 'Lochmere', 'Loudon', 'Lisbon', 'Lempster',
           'Lebanon', 'Lyme', 'Lyme Center', 'Limerick', 'Limington', 'Long Island', 'Lovell', 'Lewiston',
           'Lisbon Falls', 'Livermore', 'Livermore Falls', 'Lagrange', 'Lambert Lake', 'Levant', 'Little Deer Isle',
           'Lubec', 'Limestone', 'Lincolnville', 'Lincolnville Center', 'Liberty', 'Lake Elmore', 'Lower Waterford',
           'Lyndon', 'Lyndon Center', 'Lyndonville', 'Ledyard', 'Lakeside', 'Lake Hiawatha', 'Lincoln Park', 'Linden',
           'Livingston', 'Lyndhurst', 'Little Falls', 'Leonia', 'Little Ferry', 'Lodi', 'Leonardo', 'Lincroft',
           'Little Silver', 'Long Branch', 'Lafayette', 'Lake Hopatcong', 'Landing', 'Layton', 'Ledgewood',
           'Long Valley', 'Liberty Corner', 'Lyons', 'Lawnside', 'Lumberton', 'LEH', 'Leeds Point', 'Landisville',
           'Leesburg', 'Longport', 'Lambertville', 'Lawrence Township', 'Lakewood', 'Lakehurst', 'Lanoka Harbor',
           'Lavallette', 'Little York', 'Lake Peekskill', 'Larchmont', 'Lincolndale', 'Long Island City', 'Little Neck',
           'Locust Valley', 'Long Beach', 'Lynbrook', 'Lake Grove', 'Levittown', 'Lindenhurst', 'Laurel', 'Latham',
           'Lake Hill', 'Lake Katrine', 'Lanesville', 'Lagrangeville', 'Lake Huntington', 'Livingston Manor',
           'Loch Sheldrake', 'Long Eddy', 'Lake George', 'Lake Luzerne', 'Long Lake', 'Lake Clear', 'Lake Placid',
           'Lawrenceville', 'Lewis', 'Lyon Mountain', 'Lacona', 'La Fayette', 'Liverpool', 'Locke', 'Lycoming',
           'Lee Center', 'Leonardsville', 'Lowville', 'Lyons Falls', 'La Fargeville', 'Lorraine', 'Laurens', 'Lisle',
           'Lake View', 'Lawtons', 'Lockport', 'Le Roy', 'Lima', 'Livonia', 'Livonia Center', 'Leon', 'Lily Dale',
           'Little Genesee', 'Little Valley', 'Lakemont', 'Lindley', 'Lockwood', 'Lowman', 'Lansing', 'Langeloth',
           'Leetsdale', 'La Belle', 'Lake Lynn', 'Leckrone', 'Leisenring', 'Lemont Furnace', 'Listie', 'Larimer',
           'Latrobe', 'Laughlintown', 'Leechburg', 'Ligonier', 'Lowber', 'Loyalhanna', 'Luxor', 'La Jose',
           'Lucernemines', 'Luthersburg', 'Lilly', 'Loretto', 'Lyndora', 'Leeper', 'Lucinda', 'Lickingville',
           'Lamartine', 'Lake City', 'Linesville', 'Loysburg', 'Lewis Run', 'Lamar', 'Lanse', 'Lecontes Mills',
           'Lemont', 'Landisburg', 'Lawn', 'Lemoyne', 'Lewistown', 'Loysville', 'Lykens', 'Lemasters', 'Lurgan',
           'Lewisberry', 'Littlestown', 'Loganville', 'Lampeter', 'Leola', 'Lititz', 'Lairdsville', 'Lock Haven',
           'Loganton', 'Laurelton', 'Leck Kill', 'Lewisburg', 'Lightstreet', 'Locust Gap', 'Lavelle', 'Llewellyn',
           'Locustdale', 'Lost Creek', 'Lehigh Valley', 'Laurys Station', 'Limeport', 'Lansford', 'Lattimer Mines',
           'Lehighton', 'Long Pond', 'Lackawaxen', 'Lake Ariel', 'Lake Como', 'La Plume', 'Lenoxville', 'Laceyville',
           'Lake Harmony', 'Lake Winola', 'Laporte', 'Lehman', 'Lopez', 'Luzerne', 'Lawton', 'Le Raysville',
           'Little Meadows', 'Lahaska', 'Line Lexington', 'Lumberville', 'Langhorne', 'Lansdowne', 'Lenni',
           'Landenberg', 'Lewisville', 'Lincoln University', 'Lionville', 'Lyndell', 'Lafayette Hill', 'Lansdale',
           'Lederach', 'Leesport', 'Lenhartsville', 'Limekiln', 'Lyon Station', 'Lewes', 'Little Creek', 'Lovettsville',
           'Leonardtown', 'Lexington Park', 'Loveville', 'Lusby', 'Lanham', 'Lothian', 'Lineboro', 'Linthicum Heights',
           'Long Green', 'Lutherville Timonium', 'Lonaconing', 'Luke', 'Ladiesburg', 'Libertytown', 'Little Orleans',
           'Linkwood', 'Lorton', 'Ladysmith', 'Laneview', 'Lively', 'Locust Grove', 'Lottsburg', 'Lignum',
           'Lacey Spring', 'Linville', 'Luray', 'Locust Dale', 'Lovingston', 'Lanexa', 'Lightfoot', 'Little Plymouth',
           'Locust Hill', 'Louisa', 'Locustville', 'Lackey', 'La Crosse', 'Lambsburg', 'Laurel Fork', 'Low Moor',
           'Lynchburg', 'Lowry', 'Lynch Station', 'Lashmeet', 'Lynco', 'Lindside', 'Lake', 'Lizemores', 'London',
           'Left Hand', 'Letart', 'Looneyville', 'Levels', 'Lavalette', 'Lesage', 'Logan', 'Lorado', 'Lyburn', 'Lenore',
           'Lanark', 'Layland', 'Lester', 'Lochgelly', 'Lookout', 'Lerona', 'Leslie', 'Lorentz', 'Linn', 'Lumberport',
           'Little Birch', 'Leivasy', 'Lahmansville', 'Lost City', 'Lawsonville', 'Lowgap', 'Leasburg', 'Lillington',
           'Louisburg', 'Lewiston Woodville', 'Lucama', 'Landis', 'Lattimore', 'Lawndale', 'Lilesville', 'Lincolnton',
           'Locust', 'Lakeview', 'Laurel Hill', 'Laurinburg', 'Lemon Springs', 'Lumber Bridge', 'Lake Waccamaw',
           'Leland', 'Longwood', 'La Grange', 'Lowland', 'Lenoir', 'Laurel Springs', 'Linville Falls', 'Lake Junaluska',
           'Lake Lure', 'Lake Toxaway', 'Little Switzerland', 'Leesville', 'Liberty Hill', 'Little Mountain', 'Lugoff',
           'Lydia', 'Lodge', 'Landrum', 'Lockhart', 'Lyman', 'Ladson', 'Lane', 'Latta', 'Little River', 'Little Rock',
           'Longs', 'Loris', 'La France', 'Long Creek', 'Lowndesville', 'Lando', 'Langley', 'Lobeco', 'Lithonia',
           'Lilburn', 'Lithia Springs', 'Lindale', 'Lovejoy', 'Luthersville', 'Louisville', 'Lavonia', 'Lula', 'Lyerly',
           'Lookout Mountain', 'Lizella', 'Ludowici', 'Lumber City', 'Lakeland', 'Lake Park', 'Louvale', 'Lumpkin',
           'Lake Butler', 'Lawtey', 'Live Oak', 'Lulu', 'Lady Lake', 'Lake Geneva', 'Lanark Village', 'Lamont', 'Lloyd',
           'Lynn Haven', 'Lochloosa', 'Lake Helen', 'Lake Mary', 'Lake Monroe', 'Long Key', 'Lighthouse Point',
           'Lake Worth', 'Lake Harbor', 'Loxahatchee', 'LOX', 'Lacoochee', 'Lake Panasoffkee', 'Lithia', 'Lutz',
           'Largo', 'Lake Alfred', 'Lake Hamilton', 'Lake Wales', 'Lakeshore', 'Lorida', 'Loughman', 'Labelle',
           'Lehigh Acres', 'Longboat Key', 'Lecanto', 'Land O Lakes', 'Locust Fork', 'Leighton', 'Laceys Spring',
           'Langston', 'Lapine', 'Letohatchee', 'Luverne', 'Lineville', 'Leroy', 'Lillian', 'Loxley',
           'Lower Peach Tree', 'Lowndesboro', 'Lawley', 'Lanett', 'Loachapoka', 'Lisman', 'Lascassas', 'La Vergne',
           'Lobelville', 'Lyles', 'Lupton City', 'Laurel Bloomery', 'La Follette', 'Lancing', 'Lenoir City',
           'Lone Mountain', 'Luttrell', 'Lavinia', 'Lawrenceburg', 'Leoma', 'Lutts', 'Lynnville', 'Lake Cormorant',
           'Lambert', 'Lyon', 'Lena', 'Lorman', 'Louise', 'Lauderdale', 'Louin', 'Leakesville', 'Lucedale', 'Leary',
           'Lebanon Junction', 'Lily', 'Lejunior', 'Loyall', 'Lynch', 'Latonia', 'Lovely', 'Lowmansville', 'Lone',
           'Lick Creek', 'Leburn', 'Letcher', 'Linefork', 'Littcarr', 'La Center', 'Ledbetter', 'Lovelaceville',
           'Lowes', 'Lucas', 'Lewisport', 'Leitchfield', 'Lewis Center', 'Laurelville', 'Lithopolis', 'Lockbourne',
           'La Rue', 'Lacarne', 'Lakeside Marblehead', 'Lindsey', 'Luckey', 'Liberty Center', 'Laings', 'Lore City',
           'Lafferty', 'Lorain', 'Lakemore', 'Lake Milton', 'Leavittsburg', 'Leetonia', 'Lowellville', 'Limaville',
           'Loudonville', 'Lees Creek', 'Loveland', 'Laura', 'Ludlow Falls', 'Lucasville', 'Lynx', 'Langsville',
           'Little Hocking', 'Long Bottom', 'Lower Salem', 'Latty', 'Leipsic', 'Lapel', 'Lizton', 'Lake Village',
           'La Porte', 'Lake Station', 'Lapaz', 'Laotto', 'Larwill', 'Leo', 'Linn Grove', 'La Fontaine', 'Lagro',
           'Lake Cicott', 'Laketon', 'Leiters Ford', 'Liberty Mills', 'Logansport', 'Lucerne', 'Leavenworth',
           'Losantville', 'Linton', 'Leopold', 'Lincoln City', 'Loogootee', 'Ladoga', 'La Salle', 'Luna Pier',
           'Lake Orion', 'Leonard', 'Lapeer', 'Lennon', 'Lupton', 'Laingsburg', 'Lake Odessa', 'Lacota', 'Leonidas',
           'Ludington', 'Lake Ann', 'Lake Leelanau', 'Luther', 'Lachine', 'Levering', 'Little Lake', 'Lake Linden',
           'Lamoni', 'Le Grand', 'Liscomb', 'Lorimor', 'Lovilia', 'Lake Mills', 'Lakota', 'Latimer', 'Little Cedar',
           'Lehigh', 'Lone Rock', 'Lu Verne', 'Lytton', 'La Porte City', 'Larrabee', 'Le Mars', 'Larchwood',
           'Lidderdale', 'Lohrville', 'Little Sioux', 'La Motte', 'Luxemburg', 'Lawler', 'Lime Springs', 'Luana',
           'Ladora', 'Langworthy', 'Lost Nation', 'Lowden', 'Libertyville', 'Lockridge', 'Le Claire', 'Letts',
           'Lone Tree', 'Long Grove', 'Lannon', 'Lomira', 'Lake Delton', 'La Valle', 'Lime Ridge', 'Lyndon Station',
           'Little Chute', 'Little Suamico', 'Loyal', 'Lublin', 'Lac Du Flambeau', 'Lake Tomahawk', 'Laona', 'La Farge',
           'Lynxville', 'Lake Nebagamon', 'La Pointe', 'Luck', 'Larsen', 'Leopolis', 'Lake Elmo', 'Lindstrom',
           'Lonsdale', 'Lester Prairie', 'Lutsen', 'La Crescent', 'Lyle', 'Lake Crystal', 'Le Center', 'Le Sueur',
           'Lake Benton', 'Lakefield', 'Lake Wilson', 'Lamberton', 'Leota', 'Lismore', 'Lynd', 'Lake Lillian', 'Lucan',
           'Lastrup', 'Long Prairie', 'Lake Hubert', 'Lengby', 'Littlefork', 'Loman', 'Longville', 'Lake Bronson',
           'Lennox', 'Lesterville', 'Labolt', 'Lake Norden', 'Lake Preston', 'Lake Andes', 'Langford', 'Lower Brule',
           'Lantry', 'Lemmon', 'Little Eagle', 'Lodgepole', 'Lead', 'Lidgerwood', 'Langdon', 'Lankin', 'Larimore',
           'Lamoure', 'Lehr', 'Litchville', 'Lefor', 'Lignite', 'Lame Deer', 'Lavina', 'Lodge Grass', 'Larslan',
           'Lindsay', 'Ledger', 'Loma', 'Lothair', 'Loring', 'Lolo', 'Lonepine', 'Lake Mc Donald', 'Libby',
           'Lake Bluff', 'Lake Forest', 'Lake Villa', 'Lake Zurich', 'Lincolnshire', 'Lafox', 'Lombard',
           'Lake In The Hills', 'La Grange Park', 'Lincolnwood', 'Loda', 'Leaf River', 'Lindenwood', 'Loves Park',
           'Lynn Center', 'Ladd', 'La Moille', 'Leonore', 'Long Point', 'Lostant', 'La Harpe', 'Lomax', 'Lacon',
           'La Rose', 'London Mills', 'Lowpoint', 'Longview', 'La Place', 'Lovington', 'Lenzburg', 'La Prairie',
           'Loraine', 'Lerna', 'Lake Fork', 'Lincolns New Salem', 'Literberry', 'Loami', 'Lowder', 'Labadie', 'Liguori',
           'Lonedell', 'Luebbering', 'Laddonia', 'Louisiana', 'Lake Saint Louis', 'LSL', 'Lentner', 'Leadwood',
           'Lilbourn', 'Lowndes', 'Lees Summit', 'Lawson', 'LS', 'Levasy', 'Lone Jack', 'Lathrop', 'Laclede', 'Laredo',
           'Linneus', 'Lock Springs', 'Leeton', 'Liberal', 'Lowry City', 'Lanagan', 'La Russell', 'Laurie',
           'Lake Ozark', 'Linn Creek', 'Lohman', 'Loose Creek', 'La Monte', 'Lake Spring', 'Laquey', 'Licking',
           'Long Lane', 'Lampe', 'Lacygne', 'Lecompton', 'Leawood', 'Lenexa', 'Leonardville', 'Lebo', 'Lost Springs',
           'Longton', 'Lindsborg', 'Longford', 'Larned', 'Liebenthal', 'Lenora', 'Ludell', 'Lakin', 'Leoti', 'La Vista',
           'Leigh', 'Loup City', 'Loomis', 'Lewellen', 'Lisco', 'Long Pine', 'Lafitte', 'Luling', 'Lutcher',
           'Labadieville', 'Larose', 'Lacombe', 'Loranger', 'Lake Arthur', 'Lawtell', 'Leonville', 'Loreauville',
           'Lake Charles', 'Lacassine', 'Leblanc', 'Lettsworth', 'Lottie', 'Longstreet', 'Lake Providence', 'Lillie',
           'Lebeau', 'Lecompte', 'Libuse', 'Longleaf', 'Louann', 'Lockesburg', 'LRAFB', 'Letona', 'Lonoke',
           'Little Rock Air Force Base', 'Lambrook', 'Lepanto', 'Lexa', 'Luxora', 'Lafe', 'Leachville', 'Lead Hill',
           'Lavaca', 'Lookeba', 'Loco', 'Lone Grove', 'Leedey', 'Lone Wolf', 'Lahoma', 'Longdale', 'Lucien', 'Laverne',
           'Lenapah', 'Leflore', 'Lequire', 'Lake Dallas', 'Little Elm', 'Lavon', 'LSI', 'Ladonia', 'Lake Creek',
           'Lone Oak', 'Laird Hill', 'Laneville', 'Lone Star', 'Larue', 'Latexo', 'Leona', 'Lovelady', 'Lufkin',
           'Loving', 'Lingleville', 'Lipan', 'Lampasas', 'Little River Academy', 'Laguna Park', 'Lorena', 'Lott',
           'Lohn', 'Lometa', 'Lowake', 'Leggett', 'Lane City', 'Lissie', 'Lake Jackson', 'La Marque', 'League City',
           'La Ward', 'Lolita', 'La Coste', 'Leming', 'Lytle', 'Lakehills', 'La Vernia', 'Lackland A F B', 'La Blanca',
           'La Feria', 'La Joya', 'Lasara', 'La Villa', 'Lopeno', 'Los Ebanos', 'Los Fresnos', 'Los Indios', 'Lozano',
           'Lyford', 'Leander', 'Llano', 'Laughlin AFB', 'Langtry', 'La Pryor', 'Leakey', 'Lazbuddie', 'Lefors',
           'Lipscomb', 'Lelia Lake', 'Lockney', 'Lamesa', 'Levelland', 'Littlefield', 'Loop', 'Lorenzo', 'Lubbock',
           'Lueders', 'Lenorah', 'Larkspur', 'Louviers', 'Leadville', 'Longmont', 'Log Lane Village', 'Lindon', 'Limon',
           'La Junta', 'Las Animas', 'La Veta', 'La Jara', 'Lazear', 'Laramie', 'Lance Creek', 'Lingle', 'Lusk',
           'Lander', 'Linch', 'Lysite', 'Leiter', 'Little America', 'Lonetree', 'La Barge', 'Lava Hot Springs',
           'Leadore', 'Lemhi', 'Lapwai', 'Lucile', 'Letha', 'Laketown', 'Lapoint', 'Lehi', 'La Sal', 'Lake Powell',
           'Leamington', 'Levan', 'Lynndyl', 'La Verkin', 'Loa', 'Luke Air Force Base', 'Laveen', 'Litchfield Park',
           'Lukeville', 'Leupp', 'Lake Montezuma', 'Lake Havasu City', 'Lukachukai', 'Laguna', 'Lindrith', 'Los Lunas',
           'La Madera', 'Lamy', 'Los Alamos', 'Los Ojos', 'Las Vegas', 'La Loma', 'Lemitar', 'Luna', 'Las Cruces',
           'La Mesa', 'Lordsburg', 'Lingo', 'Loco Hills', 'La Luz', 'Logandale', 'Laughlin', 'Lund', 'Lovelock',
           'Luning', 'Lamoille', 'Los Angeles', 'LA', 'Lynwood', 'La Palma', 'La Habra', 'La Mirada', 'Lomita',
           'Los Alamitos', 'LB', 'La Canada Flintridge', 'La Crescenta', 'La Puente', 'La Verne', 'Lemon Grove',
           'Lincoln Acres', 'La Jolla', 'La Quinta', 'Landers', 'Loma Linda', 'Lake Arrowhead', 'Lucerne Valley',
           'Lytle Creek', 'Lake Elsinore', 'Laguna Niguel', 'Laguna Woods', 'Laguna Beach', 'Laguna Hills',
           'Ladera Ranch', 'Lake Isabella', 'Laton', 'Lebec', 'Lemon Cove', 'Lemoore', 'Lost Hills', 'Los Osos',
           'Lompoc', 'Los Olivos', 'Lake Hughes', 'Lee Vining', 'Littlerock', 'Lone Pine', 'Los Banos', 'La Honda',
           'Loma Mar', 'Los Altos', 'Lagunitas', 'Los Gatos', 'Lockeford', 'Long Barn', 'Lakeport', 'Laytonville',
           'Lower Lake', 'Loleta', 'Lotus', 'Lakehead', 'Los Molinos', 'Likely', 'Loyalton', 'Lahaina', 'Laie',
           'Lanai City', 'Laupahoehoe', 'Lawai', 'Lihue', 'Lake Oswego', 'Logsden', 'Langlois', 'Lorane', 'La Pine',
           'La Grande', 'Lostine', 'Lynnwood', 'La Conner', 'Lake Stevens', 'Lopez Island', 'Lummi Island', 'Lynden',
           'Lakebay', 'La Push', 'Longbranch', 'Longmire', 'Lacey', 'Lebam', 'Lilliwaup',
           'Latah', 'Liberty Lake', 'Lacrosse', 'Lamona', 'Laurier', 'Loon Lake', 'Lind', 'Larsen Bay', 'Levelock',
           'Lower Kalskag', 'Lake Minchumina']
MCities = ['Maricao', 'Manati', 'Moca', 'Mayaguez', 'Morovis', 'Maunabo', 'Mercedita', 'Monson', 'Middlefield',
           'Mill River', 'Monterey',
           'Millers Falls', 'Monroe Bridge', 'Montague', 'Manchaug', 'Millbury', 'Millville', 'Marlborough', 'Maynard',
           'Mendon', 'Milford', 'Methuen', 'Merrimac', 'Manchester', 'Marblehead', 'Middleton', 'Mansfield',
           'Marshfield', 'Marshfield Hills', 'Medfield', 'Medway', 'Millis', 'Minot', 'Mattapan', 'Malden', 'Medford',
           'Melrose', 'Milton', 'Milton Village', 'Middleboro', 'Manomet', 'Monponsett', 'Menemsha', 'Monument Beach',
           'Marstons Mills', 'Mashpee', 'Marion', 'Mattapoisett', 'Manville', 'Mapleville', 'Middletown', 'Merrimack',
           'Mont Vernon', 'Meredith', 'Moultonborough', 'Marlow', 'Milan', 'Mount Washington', 'Meriden', 'Monroe',
           'Madbury', 'Madison', 'Melvin Village', 'Milton Mills', 'Mirror Lake', 'Moody', 'Mechanic Falls', 'Mexico',
           'Monmouth', 'Mount Vernon', 'Mattawamkeag', 'Millinocket', 'Milo', 'Machias', 'Machiasport', 'Meddybemps',
           'Milbridge', 'Mount Desert', 'Madawaska', 'Mapleton', 'Mars Hill', 'Monticello', 'Matinicus', 'Monhegan',
           'Morrill', 'Mc Indoe Falls', 'Manchester Center', 'Marlboro', 'Monkton', 'Montgomery', 'Montgomery Center',
           'Montpelier', 'Moretown', 'Morrisville', 'Moscow', 'Middlebury', 'Middletown Springs', 'Mount Holly',
           'Morgan', 'Mansfield Center', 'Mansfield Depot', 'Mashantucket', 'Montville', 'Moosup', 'Mystic',
           'Middle Haddam', 'Milldale', 'Moodus', 'Morris', 'Maplewood', 'Millburn', 'Montclair', 'Mountain Lakes',
           'Moonachie', 'Mountainside', 'Mc Afee', 'Mahwah', 'Midland Park', 'Maywood', 'Montvale', 'Matawan',
           'Monmouth Beach', 'Morganville', 'Mine Hill', 'Middleville', 'Mount Arlington', 'Mount Tabor', 'Mendham',
           'Millington', 'Morris Plains', 'Morristown', 'Mount Freedom', 'Magnolia', 'Manahawkin', 'Mantua',
           'Maple Shade', 'Marlton', 'Mount Laurel', 'Medford Lakes', 'Mickleton', 'Moorestown', 'Mount Ephraim',
           'Mount Royal', 'Mullica Hill', 'Merchantville', 'Marmora', 'Malaga', 'Mauricetown', 'Mays Landing', 'Milmay',
           'Minotola', 'Mizpah', 'Monroeville', 'Margate City', 'Millstone Township', 'Manasquan', 'Mantoloking',
           'Manchester Township', 'Monroe Township', 'Martinsville', 'Metuchen', 'Middlesex', 'Milltown',
           'Monmouth Junction', 'Mahopac', 'Mahopac Falls', 'Mamaroneck', 'Maryknoll', 'Millwood', 'Mohegan Lake',
           'Montrose', 'Mount Kisco', 'Monsey', 'Mountainville', 'Manhasset', 'Maspeth', 'Middle Village', 'Mineola',
           'Malverne', 'Merrick', 'Melville', 'Massapequa', 'Massapequa Park', 'Miller Place', 'Mill Neck',
           'Mount Sinai', 'Manorville', 'Mastic', 'Mastic Beach', 'Mattituck', 'Middle Island', 'Montauk', 'Moriches',
           'Malden Bridge', 'Maryland', 'Mayfield', 'Mechanicville', 'Medusa', 'Middleburgh', 'Malden On Hudson',
           'Maplecrest', 'Margaretville', 'Mount Marion', 'Mount Tremper', 'Maybrook', 'Mellenville', 'Millbrook',
           'Millerton', 'Modena', 'Mongaup Valley', 'Mountain Dale', 'Middle Falls', 'Middle Granville', 'Middle Grove',
           'Minerva', 'Malone', 'Mineville', 'Moira', 'Mooers', 'Mooers Forks', 'Moriah', 'Moriah Center',
           'Morrisonville', 'Mc Graw', 'Mc Lean', 'Mallory', 'Manlius', 'Maple View', 'Marcellus', 'Marietta',
           'Martville', 'Memphis', 'Meridian', 'Minetto', 'Minoa', 'Montezuma', 'Moravia', 'Mottville',
           'Mc Connellsville', 'Marcy', 'Martinsburg', 'Mohawk', 'Munnsville', 'Madrid', 'Mannsville', 'Massena',
           'Mc Donough', 'Maine', 'Marathon', 'Masonville', 'Meridale', 'Mount Upton', 'Mount Vision', 'Marilla',
           'Medina', 'Middleport', 'Model City', 'Macedon', 'Morton', 'Mount Morris', 'Mumford', 'Maple Springs',
           'Mayville', 'Mecklenburg', 'Millport', 'Montour Falls', 'Mc Donald', 'Midland', 'Midway', 'Monaca',
           'Monessen', 'Monongahela', 'Mckeesport', 'Mc Kees Rocks', 'Marianna', 'Mather', 'Meadow Lands', 'Millsboro',
           'Muse', 'Mc Clellandtown', 'Markleysburg', 'Martin', 'Masontown', 'Melcroft', 'Merrittstown', 'Mill Run',
           'Mount Braddock', 'Manns Choice', 'Markleton', 'Meyersdale', 'Mammoth', 'Manor', 'Mount Pleasant',
           'Murrysville', 'Mc Intyre', 'Mahaffey', 'Mcgees Mills', 'Marchand', 'Marion Center', 'Marsteller', 'Mentcle',
           'Mineral Point', 'Mars', 'Mercer', 'Mc Grann', 'Marienville', 'Mayport', 'Marble', 'Meadville', 'Mc Kean',
           'Mill Village', 'Mc Connellstown', 'Madera', 'Morann', 'Mount Jewett', 'Madisonburg', 'Milesburg',
           'Millheim', 'Mineral Springs', 'Mingoville', 'Morrisdale', 'Moshannon', 'Munson', 'Mainesburg',
           'Middlebury Center', 'Mills', 'Morris Run', 'Mc Alisterville', 'Mechanicsburg', 'Mc Veytown',
           'Mapleton Depot', 'Marysville', 'Mattawana', 'MDT', 'Mifflin', 'Mifflintown', 'Mill Creek', 'Millersburg',
           'Millerstown', 'Milroy', 'Mount Gretna', 'Mount Holly Springs', 'Mount Union', 'Myerstown',
           'Mc Connellsburg', 'Mercersburg', 'Mont Alto', 'Mc Knightstown', 'Mc Sherrystown', 'Mount Wolf', 'Manheim',
           'Martindale', 'Maytown', 'Millersville', 'Mount Joy', 'Mountville', 'Mc Elhattan', 'Mc Ewensville',
           'Mackeyville', 'Mill Hall', 'Montoursville', 'Muncy', 'Muncy Valley', 'Marion Heights', 'Mc Clure',
           'Middleburg', 'Mifflinburg', 'Millmont', 'Montandon', 'Mount Carmel', 'Mount Pleasant Mills', 'Mahanoy City',
           'Mahanoy Plane', 'Mar Lin', 'Mary D', 'Minersville', 'Muir', 'Macungie', 'Martins Creek', 'Mcadoo',
           'Milnesville', 'Marshalls Creek', 'Matamoras', 'Millrift', 'Minisink Hills', 'Mountainhome', 'Mount Bethel',
           'Mount Pocono', 'Milanville', 'Moosic', 'Mehoopany', 'Meshoppen', 'Mifflinville', 'Mildred', 'Mountain Top',
           'Monroeton', 'Mechanicsville', 'Milford Square', 'Montgomeryville', 'Marcus Hook', 'Media', 'Merion Station',
           'Malvern', 'Mendenhall', 'Mainland', 'Mont Clare', 'Maxatawny', 'Mertztown', 'Mohnton', 'Mohrsville',
           'Monocacy Station', 'Morgantown', 'Mount Aetna', 'Montchanin', 'Marydel', 'Manassas', 'Marshall', 'Marbury',
           'Morganza', 'Mount Victoria', 'Mount Rainier', 'Montgomery Village', 'Marriottsville', 'Maryland Line',
           'Mayo', 'Middle River', 'Mc Henry', 'Midlothian', 'Mount Savage', 'Mcdaniel', 'Massey', 'Maugansville',
           'Monrovia', 'Mount Airy', 'Myersville', 'Manokin', 'Mardela Springs', 'Marion Station', 'Merrifield',
           'Merry Point', 'Mollusk', 'Montross', 'Morattico', 'Markham', 'Maurertown', 'Mitchells', 'Mc Gaheysville',
           'Mount Crawford', 'Mount Jackson', 'Mount Solon', 'Montpelier Station', 'Maidens', 'Manakin Sabot',
           'Mannboro', 'Manquin', 'Maryus', 'Mascot', 'Mathews', 'Mattaponi', 'Millers Tavern', 'Mineral', 'Moon',
           'Moseley', 'Machipongo', 'Mappsville', 'Marionville', 'Mears', 'Melfa', 'Modest Town', 'Mc Kenney',
           'Meredithville', 'Meherrin', 'Mc Coy', 'Meadows Of Dan', 'Moneta', 'Mendota', 'Max Meadows', 'Meadowview',
           'Mouth Of Wilson', 'Mc Dowell', 'Middlebrook', 'Millboro', 'Mint Spring', 'Montebello', 'Mount Sidney',
           'Mustoe', 'Madison Heights', 'Mavisdale', 'Maxie', 'Matoaka', 'Montcalm', 'Matheny', 'Maybeury', 'Marlinton',
           'Maxwelton', 'Maysel', 'Miami', 'Mount Carbon', 'Mount Olive', 'Mason', 'Millstone', 'Mount Alto', 'Midkiff',
           'Myra', 'Man', 'Mount Gay', 'Matewan', 'Maben', 'Mabscott', 'Mac Arthur', 'Mc Graws', 'Minden', 'Mount Hope',
           'Mullens', 'Meadow Bridge', 'Meadow Creek', 'Mcmechen', 'Moundsville', 'Mineral Wells', 'Macfarlan',
           'Middlebourne', 'Mount Zion', 'Munday', 'Mabie', 'Monterville', 'Meadowbrook', 'Moatsville', 'Mount Clare',
           'Maidsville', 'Mannington', 'Metz', 'Montana Mines', 'Mount Lookout', 'Mount Nebo', 'Mount Storm', 'Mathias',
           'Maysville', 'Moorefield', 'Milam', 'Mayodan', 'Mocksville', 'Mc Leansville', 'Mebane', 'Mount Gilead',
           'Macon', 'Mamers', 'Manson', 'Micro', 'Moncure', 'Macclesfield', 'Margarettsville', 'Murfreesboro',
           'Manns Harbor', 'Manteo', 'Maple', 'Merry Hill', 'Moyock', 'Mc Adenville', 'Mc Farlan', 'Marshville',
           'Matthews', 'Misenheimer', 'Mooresboro', 'Mooresville', 'Morven', 'Mount Mourne', 'Mount Ulla', 'Marston',
           'Maxton', 'Maple Hill', 'Midway Park', 'Mccutcheon Field', 'Marshallberg', 'Maury', 'Merritt',
           'Morehead City', 'Mc Grady', 'Maiden', 'Millers Creek', 'Minneapolis', 'Moravian Falls', 'Morganton',
           'Maggie Valley', 'Micaville', 'Mill Spring', 'Montreat', 'Mountain Home', 'Mills River', 'Murphy', 'Mc Bee',
           'Manning', 'Mayesville', 'Monetta', 'Moore', 'Mc Clellanville', 'Moncks Corner', 'Mc Coll', 'Myrtle Beach',
           'Mullins', 'Murrells Inlet', 'Mauldin', 'Mountain Rest', 'Mc Connells', 'Mount Croghan', 'Mc Cormick',
           'Modoc', 'Montmorenci', 'Miley', 'Mableton', 'Marble Hill', 'Mount Berry', 'Mcdonough', 'Meansville',
           'Milner', 'Molena', 'Moreland', 'Morrow', 'Metter', 'Midville', 'Millen', 'Mc Caysville', 'Mineral Bluff',
           'Mountain City', 'Murrayville', 'Maxeys', 'Menlo', 'Mesena', 'Mitchell', 'Mc Rae', 'Marshallville', 'Mauk',
           'Milledgeville', 'Musella', 'Meldrim', 'Mershon', 'Moody AFB', 'Meigs', 'Moultrie', 'Mc Alpin', 'Macclenny',
           'Mexico Beach', 'Mossy Head', 'Milligan', 'Miramar Beach', 'Mc David', 'Mary Esther', 'Molino', 'Mc Intosh',
           'Micanopy', 'Morriston', 'Mid Florida', 'Maitland', 'Mims', 'Mount Dora', 'Melbourne', 'Malabar',
           'Melbourne Beach', 'Merritt Island', 'Marathon Shores', 'Miami Gardens', 'Margate', 'Miami Beach',
           'Moore Haven', 'Mango', 'Mulberry', 'Murdock', 'Marco Island', 'Myakka City', 'Mascotte', 'Minneola',
           'Montverde', 'Mc Calla', 'Margaret', 'Maylene', 'Montevallo', 'Mulga', 'Mc Shan', 'Moundville', 'Moulton',
           'Muscle Shoals', 'Meridianville', 'Mentone', 'Mount Meigs', 'Millerville', 'Munford', 'Muscadine',
           'Midland City', 'Mc Kenzie', 'Megargel', 'Mexia', 'Magnolia Springs', 'Malcolm', 'Millry', 'Mobile',
           'Maplesville', 'Mc Williams', 'Marion Junction', 'Minter', 'Morvin', 'Myrtlewood', 'Melvin', 'Mc Ewen',
           'Mcminnville', 'Mitchellville', 'Mount Juliet', 'Madisonville', 'Monteagle', 'Morrison', 'Milligan College',
           'Maryville', 'Maynardville', 'Mooresburg', 'Mosheim', 'Maury City', 'Mc Lemoresville', 'Medon', 'Michie',
           'Morris Chapel', 'Minor Hill', 'Moss', 'Marks', 'Michigan City', 'Myrtle', 'Merigold', 'Metcalfe',
           'Moorhead', 'Mound Bayou', 'Mantachie', 'Mooreville', 'Mc Carley', 'Minter City', 'Money', 'Morgan City',
           'Mc Adams', 'Mc Cool', 'Madden', 'Magee', 'Mayersville', 'Midnight', 'Mize', 'Mc Lain', 'Mc Neill',
           'Moselle', 'Moss Point', 'Mc Call Creek', 'Mccomb', 'Mantee', 'Mathiston', 'Mayhew', 'Mississippi State',
           'MSU', 'Mackville', 'Masonic Home', 'Mount Eden', 'Mc Daniels', 'Mc Quady', 'Muldraugh', 'Means', 'Morehead',
           'Mount Sterling', 'Mc Kee', 'Mc Kinney', 'Mitchellsburg', 'Miracle', 'Mozelle', 'Mary Alice', 'Middlesboro',
           'Mayslick', 'Morning View', 'Mount Olivet', 'Muses Mills', 'Martha', 'Mazie', 'Meally', 'Mistletoe',
           'Mc Andrews', 'Mc Carr', 'Majestic', 'Mouthcard', 'Minnie', 'Mc Roberts', 'Mallie', 'Mayking', 'Mousie',
           'Melber', 'Milburn', 'Murray', 'Mount Hermon', 'Mammoth Cave', 'Maceo', 'Maple Mount', 'Manitou',
           'Morganfield', 'Mortons Gap', 'Marshes Siding', 'Marrowbone', 'Mount Sherman', 'Munfordville',
           'Magnetic Springs', 'Milford Center', 'Millersport', 'Mingo', 'Mount Liberty', 'Murray City', 'Marengo',
           'Martel', 'Morral', 'Mount Victory', 'Middle Bass', 'Malinta', 'Mark Center', 'Maumee', 'Metamora',
           'Milton Center', 'Monclova', 'Mcconnelsville', 'Malta', 'Mount Perry', 'Moxahala', 'Martins Ferry',
           'Mingo Junction', 'Macedonia', 'Mentor', 'MOL', 'Maple Heights', 'Mogadore', 'Munroe Falls', 'Masury',
           'Mesopotamia', 'Mineral Ridge', 'Massillon', 'Maximo', 'Mechanicstown', 'Middlebranch', 'Midvale',
           'Mineral City', 'Mount Eaton', 'Mc Cutchenville', 'Melmore', 'Maineville', 'Miamitown', 'Mount Saint Joseph',
           'Miamiville', 'Mount Orab', 'Mowrystown', 'Miamisburg', 'Mc Arthur', 'Mc Dermott', 'Minford', 'Macksburg',
           'Millfield', 'Mc Comb', 'Mc Guffey', 'Maria Stein', 'Middle Point', 'Miller City', 'Minster',
           'Mount Blanchard', 'Mount Cory', 'Mc Cordsville', 'Markleville', 'Michigantown', 'Manilla', 'Maxwell',
           'Mays', 'Munster', 'Merrillville', 'Mishawaka', 'Markle', 'Mongo', 'Macy', 'Moores Hill', 'Mauckport',
           'Mount Saint Francis', 'Medora', 'Millhousen', 'Muncie', 'Mooreland', 'Mount Summit', 'Mariah Hill',
           'Monroe City', 'Mackey', 'Mecca', 'Merom', 'Medaryville', 'Mellott', 'Monon', 'Morocco', 'Mount Ayr',
           'Marine City', 'Macomb', 'Mount Clemens', 'Melvindale', 'Maybee', 'Marlette', 'Minden City', 'Merrill',
           'Mio', 'Mikado', 'Munger', 'Mcbrides', 'Maple Rapids', 'Morrice', 'Mulliken', 'Mattawan', 'Manitou Beach',
           'Michigan Center', 'Morenci', 'Mosherville', 'Munith', 'Mecosta', 'Moline', 'Morley', 'Macatawa', 'Marne',
           'Muskegon', 'Mc Bain', 'Mancelona', 'Manistee', 'Manton', 'Maple City', 'Mesick', 'Mackinaw City',
           'Mackinac Island', 'Moran', 'Mullett Lake', 'Mc Millan', 'Manistique', 'Marquette', 'Menominee',
           'Michigamme', 'Munising', 'Marenisco', 'Mass City', 'Melcher Dallas', 'Mc Callsburg', 'Malcom',
           'Marshalltown', 'Martensdale', 'Minburn', 'Montour', 'Mason City', 'Mc Intire', 'Manly', 'Meservey',
           'Mallard', 'Moorland', 'Marble Rock', 'Marcus', 'Maurice', 'Moville', 'Matlock', 'Mc Clelland',
           'Missouri Valley', 'Modale', 'Mondamin', 'Maquoketa', 'Miles', 'Mc Gregor', 'Monona', 'Martelle',
           'Middle Amana', 'Mount Auburn', 'Mediapolis', 'Morning Sun', 'Mc Causland', 'Muscatine', 'Menomonee Falls',
           'Merton', 'Mount Calvary', 'Mequon', 'Mukwonago', 'Muskego', 'Milwaukee', 'Mc Farland', 'Mazomanie',
           'Montfort', 'Mount Horeb', 'Muscoda', 'Markesan', 'Mauston', 'Montello', 'Marinette', 'Mountain',
           'Manitowoc', 'Maribel', 'Mishicot', 'Mattoon', 'Milladore', 'Mosinee', 'Mc Naughton', 'Manitowish Waters',
           'Mellen', 'Minocqua', 'Montreal', 'Millston', 'Mindoro', 'Maiden Rock', 'Menomonie', 'Merrillan', 'Mondovi',
           'Mikana', 'Minong', 'Manawa', 'Menasha', 'Marine On Saint Croix', 'Mora', 'Minnetonka', 'Maple Plain',
           'Maple Lake', 'Mayer', 'Minnetonka Beach', 'Mound', 'Mcgregor', 'Makinen', 'Meadowlands', 'Melrude',
           'Moose Lake', 'Mountain Iron', 'Mabel', 'Mantorville', 'Mazeppa', 'Minnesota City', 'Mankato', 'Madelia',
           'Madison Lake', 'Minnesota Lake', 'Mountain Lake', 'Minneota', 'Montevideo', 'Mc Grath', 'Milaca', 'Miltona',
           'Menahga', 'Motley', 'Mcintosh', 'Mahnomen', 'Marcell', 'Margie', 'Max', 'Menno', 'Mission Hill', 'Marvin',
           'Milbank', 'Marty', 'Miller', 'Mellette', 'Milesville', 'Mission', 'Murdo', 'Mobridge', 'Mc Laughlin',
           'Meadow', 'Mound City', 'Manderson', 'Mud Butte', 'Mcleod', 'Mantador', 'Milnor', 'Mooreton', 'Mcville',
           'Maida', 'Manvel', 'Mekinock', 'Michigan', 'Minto', 'Maddock', 'Minnewaukan', 'Munich', 'Mylo', 'Mcclusky',
           'Mchenry', 'Mandan', 'Menoken', 'Moffit', 'Marmarth', 'Mott', 'Minot AFB', 'MAFB', 'Makoti', 'Mandaree',
           'Maxbass', 'Mohall', 'Mc Leod', 'Martinsdale', 'Melstone', 'Molt', 'Mosby', 'Musselshell', 'Medicine Lake',
           'Miles City', 'Malmstrom AFB', 'Moccasin', 'Monarch', 'Mc Allister', 'Manhattan', 'Missoula', 'Martin City',
           'Morton Grove', 'Mount Prospect', 'Mundelein', 'Maple Park', 'Medinah', 'Melrose Park', 'Matteson', 'Mazon',
           'Minooka', 'Mokena', 'Monee', 'Mooseheart', 'Manteno', 'Martinton', 'Momence', 'Mc Connell', 'Monroe Center',
           'Mount Carroll', 'Machesney Park', 'Matherville', 'Mc Nabb', 'Mark', 'Marseilles', 'Maquon', 'Manito',
           'Mossville', 'Mackinaw', 'Maroa', 'Merna', 'Minier', 'Minonk', 'Mahomet', 'Milmine', 'Metcalf', 'Marine',
           'Michael', 'Moro', 'Mozier', 'Maeystown', 'Marissa', 'Mascoutah', 'Menard', 'Millstadt', 'Mulberry Grove',
           'Mode', 'Mount Erie', 'Mount Pulaski', 'Mt Zion', 'Moweaqua', 'Meredosia', 'Modesto', 'Mc Leansboro',
           'Maunie', 'Mill Shoals', 'Mulkeytown', 'Makanda', 'Metropolis', 'Millcreek', 'Mounds', 'Muddy',
           'Murphysboro', 'Maryland Heights', 'Mapaville', 'Morse Mill', 'Marthasville', 'Montgomery City',
           'Moscow Mills', 'Marquand', 'Middle Brook', 'Mc Gee', 'Mc Bride', 'Morehouse', 'Mayview', 'Missouri City',
           'Mc Fall', 'Marceline', 'Mindenmines', 'Mc Girk', 'Meta', 'Mokane', 'Moberly', 'Malta Bend', 'Montier',
           'Mountain View', 'Mc Clurg', 'Monett', 'Mountain Grove', 'Macks Creek', 'Mc Louth', 'Muscotah', 'Mayetta',
           'Melvern', 'Mc Cune', 'Matfield Green', 'Mahaska', 'Morrowville', 'Munden', 'Maize', 'Medicine Lodge',
           'Moundridge', 'Mullinville', 'Mulvane', 'Mcconnell AFB', 'Mound Valley', 'Mcpherson', 'Miltonvale',
           'Mc Cracken', 'Macksville', 'Morland', 'Monument', 'Manter', 'Marienthal', 'Meade', 'Malmo', 'Mead',
           'Mc Cool Junction', 'Manley', 'Martell', 'Morse Bluff', 'Mclean', 'Magnet', 'Maskell', 'Meadow Grove',
           'Mc Cook', 'Mullen', 'Merriman', 'Mcgrew', 'Marsland', 'Melbeta', 'Minatare', 'Metairie', 'Marrero',
           'Meraux', 'Montegut', 'Mandeville', 'Maurepas', 'Mamou', 'Mermentau', 'Morse', 'Merryville', 'Mittie',
           'Maringouin', 'Mooringsport', 'Mangham', 'Mer Rouge', 'Mansura', 'Marksville', 'Moreauville', 'Many',
           'Marthaville', 'Mc Gehee', 'Mc Neil', 'Mc Caskill', 'Mena', 'Mountain Pine', 'Mount Ida', 'Mc Crory',
           'Mabelvale', 'Mayflower', 'Menifee', 'Morrilton', 'Maumelle', 'Marked Tree', 'Marvell', 'Mellwood',
           'Mc Dougal', 'Manila', 'Marmaduke', 'Minturn', 'Monette', 'Magness', 'Mammoth Spring', 'Marcella',
           'Marble Falls', 'Mount Judea', 'Magazine', 'Mountainburg', 'Minco', 'Mulhall', 'Mustang', 'Madill', 'Mangum',
           'Medicine Park', 'Meers', 'Mountain Park', 'Meno', 'May', 'Mutual', 'Mannford', 'Maramec', 'Milfay',
           'Muskogee', 'Moodys', 'Mcalester', 'Moyers', 'Marland', 'Mcloud', 'Maud', 'Meeker', 'Mccurtain',
           'Marble City', 'Moffett', 'Muldrow', 'Mckinney', 'Mabank', 'Malakoff', 'Mesquite', 'Melissa', 'Merit',
           'Mount Enterprise', 'Maydelle', 'Murchison', 'Montalba', 'Maypearl', 'Millsap', 'Muenster', 'Mingus',
           'Morgan Mill', 'Milano', 'Marlin', 'Mart', 'Mertens', 'Mount Calm', 'Millersview', 'Mullin', 'Mereta',
           'Mertzon', 'Matagorda', 'Midfield', 'Mont Belvieu', 'Mauriceville', 'Marquez', 'Millican', 'Mcfaddin',
           'Meyersville', 'Macdona', 'Mico', 'Mc Queeney', 'Mathis', 'Mirando City', 'Mcallen', 'Mercedes', 'Mc Dade',
           'Manchaca', 'Muldoon', 'Masterson', 'Mobeetie', 'Matador', 'Muleshoe', 'Mc Caulley', 'Maryneal', 'Merkel',
           'Mc Camey', 'Monahans', 'Marfa', 'Milliken', 'Merino', 'Manitou Springs', 'Matheson', 'Mc Clave',
           'Manzanola', 'Model', 'Manassa', 'Moffat', 'Monte Vista', 'Mosca', 'Mancos', 'Marvel',
           'Mesa Verde National Park', 'Mack', 'Maybell', 'Mesa', 'Molina', 'Medicine Bow', 'Meeteetse', 'Midwest',
           'Moorcroft', 'Mc Kinnon', 'Moose', 'Mccammon', 'Mackay', 'Malad City', 'Minidoka', 'Murtaugh', 'Macks Inn',
           'Menan', 'Monteview', 'Mccall', 'Marsing', 'Melba', 'Mountain Home AFB', 'Medimont', 'Moyie Springs',
           'Mullan', 'Magna', 'Myton', 'MSC', 'Mexican Hat', 'Moab', 'Montezuma Creek', 'Monument Valley', 'Manti',
           'Mona', 'Moroni', 'Marysvale', 'Maricopa', 'Mc Neal', 'Mount Lemmon', 'Marana', 'Mcnary', 'Munds Park',
           'Marble Canyon', 'Mormon Lake', 'Mohave Valley', 'Meadview', 'Many Farms', 'Moriarty', 'Mountainair',
           'Mentmore', 'Mexican Springs', 'Medanales', 'Mosquero', 'Magdalena', 'Mesilla', 'Mesilla Park', 'Mimbres',
           'Mule Creek', 'Milnesand', 'Mcdonald', 'Maljamar', 'Mayhill', 'Mescalero', 'Mcalister', 'Mercury', 'Moapa',
           'Mc Gill', 'Mc Dermitt', 'Mina', 'Malibu', 'Manhattan Beach', 'Marina Del Rey', 'Mount Wilson',
           'Mission Hills', 'Mira Loma', 'Monterey Park', 'Mt Baldy', 'Mount Laguna', 'Morongo Valley', 'Mountain Pass',
           'March Air Reserve Base', 'Moreno Valley', 'Mountain Center', 'Murrieta', 'Midway City', 'Mission Viejo',
           'Moorpark', 'Mc Kittrick', 'Morro Bay', 'Mojave', 'Mammoth Lakes', 'Miramonte', 'Mono Hot Springs', 'Marina',
           'Menlo Park', 'Millbrae', 'Montara', 'Moss Beach', 'Martinez', 'Moraga', 'Mill Valley', 'Milpitas',
           'Morgan Hill', 'Moss Landing', 'Mount Hamilton', 'Mokelumne Hill', 'Mountain Ranch', 'Murphys', 'Manteca',
           'Mariposa', 'Merced', 'Midpines', 'Mi Wuk Village', 'Mendocino', 'Monte Rio', 'Mckinleyville', 'Mad River',
           'Miranda', 'Myers Flat', 'Mcclellan', 'Mount Aukum', 'Meadow Vista', 'Magalia', 'Meadow Valley', 'Mcarthur',
           'Mccloud', 'Macdoel', 'Montgomery Creek', 'Mount Shasta', 'Madeline', 'Markleeville', 'Makawao', 'Makaweli',
           'Maunaloa', 'Mililani', 'Mcbh Kaneohe Bay', 'Merizo', 'Mangilao', 'Majuro', 'Marylhurst', 'Maupin',
           'Molalla', 'Mosier', 'Mount Hood Parkdale', 'Mulino', 'Manzanita', 'Mill City', 'Mount Angel', 'Mehama',
           'Marcola', 'Myrtle Creek', 'Myrtle Point', 'Merlin', 'Malin', 'Madras', 'Meacham', 'Mikkalo',
           'Milton Freewater', 'Maple Valley', 'Mercer Island', 'Mountlake Terrace', 'Maple Falls', 'Marblemount',
           'Mukilteo', 'Mcchord AFB', 'Mccleary', 'Mckenna', 'Moclips', 'Montesano', 'Mossyrock', 'Malott', 'Mazama',
           'Methow', 'Monitor', 'Moses Lake', 'Mabton', 'Moxee', 'Medical Lake', 'Mica', 'Malo', 'Metaline',
           'Metaline Falls',
           'Mohler', 'Mattawa', 'Manokotak', 'Mekoryuk', 'Moose Pass', 'Mountain Village', 'Manley Hot Springs',
           'Meyers Chuck', 'Metlakatla']
NCities = ['Naguabo', 'Naranjito', 'North Amherst', 'Northampton', 'North Hatfield', 'North Adams', 'North Egremont',
           'New Salem', 'Northfield',
           'New Braintree', 'Northborough', 'Northbridge', 'North Brookfield', 'North Grafton', 'North Oxford',
           'North Uxbridge', 'Natick', 'North Andover',
           'North Billerica', 'North Chelmsford', 'North Reading', 'Nutting Lake', 'Nahant', 'Newburyport', 'Newbury',
           'Norfolk', 'North Marshfield', 'North Scituate',
           'Norwell', 'Norwood', 'North Weymouth', 'North Carver', 'North Easton', 'North Pembroke', 'North Waltham',
           'New Town', 'Newton', 'Newton Center', 'Newtonville', 'Newton Highlands', 'Newton Lower Falls',
           'Newton Upper Falls', 'Needham', 'Needham Heights', 'Nonantum', 'Nantucket', 'North Falmouth',
           'North Chatham', 'North Eastham', 'North Truro', 'New Bedford', 'North Dartmouth', 'North Attleboro',
           'North Dighton', 'Norton', 'Newport', 'NETC', 'North Kingstown', 'Narragansett', 'North Smithfield',
           'North Providence', 'Nashua', 'New Boston', 'New Ipswich', 'North Salem', 'New Hampton', 'New London',
           'North Sandwich', 'North Sutton', 'Northwood', 'North Woodstock', 'Nottingham', 'Nelson', 'Northumberland',
           'North Stratford', 'North Walpole', 'North Haverhill', 'Newington', 'New Castle', 'New Durham', 'Newfields',
           'Newmarket', 'Newton Junction', 'North Conway', 'North Hampton', 'North Berwick', 'Naples', 'Newfield',
           'North Bridgton', 'North Waterboro', 'North Yarmouth', 'New Gloucester', 'Newry', 'North Jay',
           'North Monmouth', 'North Turner', 'North Waterford', 'Norway', 'Newcastle', 'New Harbor', 'Nobleboro',
           'Northeast Harbor', 'New Limerick', 'New Sweden', 'North Haven', 'New Portland', 'New Sharon',
           'New Vineyard', 'Norridgewock', 'North Anson', 'North Vassalboro', 'North Hartland', 'North Pomfret',
           'North Thetford', 'Norwich', 'North Springfield', 'North Bennington', 'North Pownal', 'Newfane', 'New Haven',
           'North Ferrisburgh', 'North Hero', 'Northfield Falls', 'North Hyde Park', 'North Montpelier',
           'North Clarendon', 'Newport Center', 'North Concord', 'North Troy', 'New Britain', 'New Hartford',
           'North Canton', 'North Granby', 'North Franklin', 'North Grosvenordale', 'North Windham', 'Niantic',
           'North Stonington', 'Newtown', 'North Branford', 'Northford', 'North Westchester', 'Naugatuck',
           'New Milford', 'New Preston Marble Dale', 'New Fairfield', 'New Canaan', 'Norwalk', 'North Arlington',
           'North Bergen', 'Newark', 'Nutley', 'Newfoundland', 'Northvale', 'Navesink', 'Neptune', 'Netcong',
           'New Providence', 'New Vernon', 'National Park', 'New Lisbon', 'New Gretna', 'Norma', 'New Egypt',
           'Normandy Beach', 'Neshanic Station', 'New Brunswick', 'North Brunswick', 'New York', 'New Rochelle',
           'Nanuet', 'New City', 'Nyack', 'New Hyde Park', 'North Babylon', 'Nesconset', 'Northport', 'New Suffolk',
           'Nassau', 'New Baltimore', 'New Lebanon', 'Niverville', 'North Blenheim', 'North Hoosick', 'Northville',
           'Napanoch', 'New Kingston', 'Newburgh', 'New Windsor', 'New Paltz', 'Narrowsburg', 'Neversink',
           'North Branch', 'Newcomb', 'North Creek', 'North Granville', 'North Hudson', 'North River', 'New Russia',
           'Nicholville', 'North Bangor', 'North Lawrence', 'Nedrow', 'New Woodstock', 'North Bay', 'North Pitcher',
           'Nelliston', 'New Berlin', 'New York Mills', 'Natural Bridge', 'Newton Falls', 'Newark Valley', 'Nichols',
           'Nineveh', 'North Norwich', 'Niagara University', 'North Boston', 'North Collins', 'North Evans',
           'North Java', 'North Tonawanda', 'Niagara Falls', 'North Chili', 'North Greece', 'North Rose', 'Nunda',
           'Niobe', 'Natrona Heights', 'New Brighton', 'New Eagle', 'New Kensington', 'North Versailles', 'Nemacolin',
           'New Freeport', 'Newell', 'New Geneva', 'Normalville', 'New Paris', 'New Alexandria', 'New Derry',
           'New Stanton', 'North Apollo', 'Norvelt', 'Northern Cambria', 'Nicktown', 'Northpoint', 'Nanty Glo',
           'New Florence', 'North Washington', 'New Galilee', 'New Wilmington', 'New Bethlehem', 'Nu Mine',
           'North East', 'New Enterprise', 'New Millport', 'New Bloomfield', 'New Buffalo', 'New Cumberland',
           'New Germantown', 'New Kingstown', 'Newmanstown', 'Newton Hamilton', 'Needmore', 'Neelyton', 'Newburg',
           'Newville', 'New Freedom', 'New Oxford', 'New Park', 'Narvon', 'New Holland', 'North Bend', 'New Columbia',
           'Numidia', 'New Philadelphia', 'New Ringgold', 'Nazareth', 'Neffs', 'New Tripoli', 'Nesquehoning',
           'Nuremberg', 'Nicholson', 'Nanticoke', 'Nescopeck', 'Noxen', 'New Albany', 'New Hope', 'Narberth',
           'Newtown Square', 'Norristown', 'North Wales', 'New Berlinville', 'Nokesville', 'Naval Anacost Annex',
           'Nanjemoy', 'North Beach', 'Neavitt', 'New Market', 'New Midway', 'Ninde', 'Nuttsville', 'Nellysford',
           'North Garden', 'New Canton', 'New Kent', 'New Point', 'Norge', 'North', 'Nassawadox', 'Nelsonia',
           'New Church', 'Newport News', 'NASA', 'Newsoms', 'Nottoway', 'Narrows', 'Newbern', 'New River',
           'Nickelsville', 'Nora', 'Naruna', 'Nathalie', 'Natural Bridge Station', 'North Tazewell', 'Nemours',
           'Newhall', 'New Richmond', 'Northfork', 'North Spring', 'Naoma', 'Nebo', 'Nellis', 'Nitro', 'Normantown',
           'North Matewan', 'Nimitz', 'New Manchester', 'New Martinsville', 'New Milton', 'Napier', 'Nallen', 'Nettie',
           'New Creek', 'New Hill', 'Norlina', 'Nashville', 'Nags Head', 'Newton Grove', 'Norman', 'Nakina', 'New Bern',
           'North Wilkesboro', 'Newland', 'Neeses', 'Newberry', 'New Zion', 'North Charleston', 'Nesmith',
           'North Myrtle Beach', 'Ninety Six', 'Norris', 'New Ellenton', 'North Augusta', 'Norcross', 'North Metro',
           'Newborn', 'Newnan', 'Nunez', 'Nahunta', 'Nicholls', 'Naylor', 'Norman Park', 'New Smyrna Beach',
           'Neptune Beach', 'Noma', 'Navarre', 'Niceville', 'North Miami Beach', 'North Palm Beach', 'Nalcrest',
           'North Fort Myers', 'Nocatee', 'Nokomis', 'North Port', 'New Port Richey', 'Nobleton', 'Nauvoo', 'Normal',
           'New Brockton', 'Nanafalia', 'Notasulga', 'New Johnsonville', 'Nolensville', 'Norene', 'Nunnelly',
           'Normandy', 'New Tazewell', 'Niota', 'Nesbit', 'Nettleton', 'New Site', 'North Carrollton', 'Natchez',
           'Newhebron', 'Noxapater', 'Neely', 'New Augusta', 'N S T L', 'Nerinx', 'Nicholasville', 'New Liberty',
           'North Middletown', 'Neon', 'New Concord', 'Nortonville', 'Nancy', 'North Lewisburg', 'New Bloomington',
           'Napoleon', 'Neapolis', 'New Bavaria', 'Ney', 'New Lexington', 'New Straitsville', 'Nashport',
           'Newcomerstown', 'New Athens', 'New Rumley', 'North Ridgeville', 'North Kingsville', 'North Olmsted',
           'Novelty', 'North Royalton', 'Negley', 'New Middletown', 'New Springfield', 'New Waterford', 'Niles',
           'North Benton', 'North Bloomfield', 'North Jackson', 'North Lima', 'North Georgetown', 'Nankin', 'Nevada',
           'New Riegel', 'New Washington', 'North Fairfield', 'North Robinson', 'Nova', 'Neville', 'Newtonsville',
           'New Vienna', 'New Carlisle', 'New Madison', 'New Weston', 'North Star', 'New Plymouth', 'Nelsonville',
           'New Marshfield', 'New Matamoras', 'New Bremen', 'New Hampshire', 'New Knoxville', 'North Baltimore',
           'Noblesville', 'New Palestine', 'North Judson', 'Nappanee', 'North Liberty', 'North Webster', 'Notre Dame',
           'New Waverly', 'North Manchester', 'New Trenton', 'Nabb', 'New Salisbury', 'North Vernon', 'New Harmony',
           'New Goshen', 'New Ross', 'North Street', 'New Hudson', 'Novi', 'New Lothrop', 'National City', 'Nottawa',
           'New Troy', 'Norvell', 'Newaygo', 'New Era', 'Nunica', 'Naubinway', 'Nadeau', 'Nahma', 'National Mine',
           'Negaunee', 'Nisula', 'New Virginia', 'Nora Springs', 'Nemaha', 'Nodaway', 'Neola', 'Northboro',
           'North Buena Vista', 'New Albin', 'North English', 'Nashotah', 'Neosho', 'New Holstein', 'North Lake',
           'New Munster', 'North Prairie', 'New Glarus', 'North Freedom', 'Neopit', 'Niagara', 'New Franken',
           'Neillsville', 'Nekoosa', 'Necedah', 'New Auburn', 'Neenah', 'Neshkoro', 'Nerstrand', 'New Germany', 'NYA',
           'Norwood Young America', 'Nashwauk', 'Nett Lake', 'New Prague', 'New Richland', 'New Ulm', 'Nicollet',
           'Northrop', 'New Munich', 'Nevis', 'Nisswa', 'Nimrod', 'Naytahwaush', 'Nielsville', 'Northome', 'Newfolden',
           'Noyes', 'North Sioux City', 'New Effington', 'Nemo', 'New Underwood', 'Nisland', 'Nome', 'Neche', 'Nekoma',
           'New Rockford', 'New Leipzig', 'New England', 'Noonan', 'Nye', 'Neihart', 'Noxon', 'Northbrook',
           'North Chicago', 'New Lenox', 'Naperville', 'North Aurora', 'Nachusa', 'Neponset', 'North Henderson',
           'Newman', 'National Stock Yards', 'New Douglas', 'New Baden', 'New Memphis', 'Neoga', 'Nilwood', 'Nason',
           'Noble', 'Norris City', 'New Burnside', 'New Melle', 'New Cambria', 'Novinger', 'New Madrid', 'Neelyville',
           'N KC', 'NKC', 'Norborne', 'Neck City', 'Newtonia', 'Noel', 'New Franklin', 'Niangua', 'Nixa', 'New Century',
           'Netawaka', 'Neodesha', 'Neosho Falls', 'Neal', 'Neosho Rapids', 'Narka', 'North Newton', 'Niotaze',
           'Ness City', 'Nickerson', 'Natoma', 'Norcatur', 'Nebraska City', 'Nehawka', 'Naper', 'Neligh',
           'Newman Grove', 'Niobrara', 'North Loup', 'Naponee', 'North Platte', 'Nenzel', 'New Sarpy', 'Norco',
           'New Orleans', 'Napoleonville', 'Natalbany', 'New Iberia', 'New Roads', 'Newellton', 'NSU', 'Natchitoches',
           'Negreet', 'New Llano', 'New Edinburg', 'Norphlet', 'Newhope', 'North Little Rock', 'N LR', 'Norfork',
           'New Blaine', 'Natural Dam', 'Nicoma Park', 'Ninnekah', 'Nash', 'Nowata', 'North Miami', 'Nashoba', 'Nardin',
           'Newkirk', 'Newalla', 'Neches', 'New Summerfield', 'Nacogdoches', 'Naval Air Station/ Jrb', 'NAS/JRB',
           'North Richland Hills', 'Nocona', 'Nolanville', 'North Houston', 'New Caney', 'Nada', 'Needville',
           'Nederland', 'Navasota', 'Normangee', 'North Zulch', 'Nursery', 'Natalia', 'New Braunfels', 'Nixon',
           'Nordheim', 'Normanna', 'New Deal', 'New Home', 'Nolan', 'Novice', 'Notrees', 'Niwot', 'Nunn', 'New Raymer',
           'Nathrop', 'Naturita', 'Nucla', 'Natrona', 'Newdale', 'North Fork', 'Nezperce', 'Nampa', 'New Meadows',
           'Notus', 'Nordman', 'North Salt Lake', 'NSL', 'Nephi', 'Naco', 'Nogales', 'Nutrioso', 'NAU', 'North Rim',
           'Nazlini', 'Nageezi', 'New Laguna', 'Navajo', 'Navajo Dam', 'Nogal', 'Nara Visa', 'North Las Vegas',
           'Nellis AFB', 'Newbury Park', 'Northridge', 'North Hills', 'North Hollywood', 'Niland', 'North Palm Springs',
           'Needles', 'Nipton', 'Newberry Springs', 'Nuevo', 'Newport Coast', 'Newport Beach', 'New Cuyama', 'Nipomo',
           'Napa', 'Novato', 'Nicasio', 'New Almaden', 'Navarro', 'Nice', 'Nicolaus', 'North Highlands', 'Norden',
           'Nevada City', 'North San Juan', 'Nubieber', 'Naalehu', 'Ninole', 'Nehalem', 'Newberg', 'North Plains',
           'Netarts', 'Neskowin', 'Neotsu', 'Noti', 'New Pine Creek', 'North Powder', 'Nyssa', 'North Lakewood',
           'Nooksack', 'Neah Bay', 'Nordland', 'Napavine', 'Neilton', 'Nahcotta', 'Naselle', 'North Bonneville',
           'Naches', 'Newman Lake', 'Nine Mile Falls', 'Nespelem', 'Naknek', 'Napakiak', 'Nikiski', 'New Stuyahok',
           'Nikolski',
           'Ninilchik', 'Nondalton', 'Nunapitchuk', 'Nunam Iqua', 'Nightmute', 'Nikolai', 'North Pole', 'Nenana',
           'Noatak', 'Noorvik', 'Northway', 'Nulato', 'Nuiqsut']
OCities = ['Orocovis', 'Oakham', 'Otis', 'Orange', 'Oxford', 'Ocean Bluff', 'Oak Bluffs', 'Onset', 'Orleans',
           'Osterville', 'Oakland',
           'Orford', 'Ossipee', 'Ogunquit', 'Ocean Park', 'Old Orchard Beach', 'Orrs Island', 'Old Town', 'Orono',
           'Orient', 'Orland', 'Orrington', 'Oakfield', 'Oxbow', 'Owls Head', 'Oquossoc', 'Orwell', 'Oakdale',
           'Old Lyme', 'Old Mystic', 'Oneco', 'Old Saybrook', 'Oakville', 'Old Greenwich', 'Oak Ridge', 'Ogdensburg',
           'Oradell', 'Oakhurst', 'Ocean Grove', 'Oceanport', 'Oaklyn', 'Ocean City', 'Ocean View', 'Oceanville',
           'Ocean Gate', 'Old Bridge', 'Oldwick', 'Ossining', 'Orangeburg', 'Otisville', 'Oakland Gardens',
           'Ozone Park', 'Old Westbury', 'Oceanside', 'Ocean Beach', 'Oyster Bay', 'Old Bethpage', 'Old Chatham',
           'Oak Hill', 'Olivebridge', 'Obernburg', 'Olmstedville', 'Oswego', 'Old Forge', 'Oneida', 'Oriskany',
           'Oriskany Falls', 'Oswegatchie', 'Oneonta', 'Otego', 'Ouaquaga', 'Owego', 'Olcott', 'Orchard Park',
           'Oaks Corners', 'Ontario', 'Ontario Center', 'Ovid', 'Olean', 'Otto', 'Odessa', 'Oakmont', 'Ohiopyle',
           'Oliver', 'Oliveburg', 'Oil City', 'Osceola Mills', 'Osterburg', 'Olanta', 'Orviston', 'Osceola',
           'Oakland Mills', 'Ono', 'Orbisonia', 'Orrstown', 'Orrtanna', 'Orangeville', 'Orwigsburg', 'Old Zionsville',
           'Orefield', 'Olyphant', 'Orson', 'Ottsville', 'Oreland', 'Oaks', 'Oley', 'Orlean', 'Owings', 'Oxon Hill',
           'Olney', 'Odenton', 'Owings Mills', 'Oldtown', 'Oakton', 'Occoquan', 'Oldhams', 'Ophelia', 'Oakpark',
           'Orkney Springs', 'Oilville', 'Onemo', 'Ordinary', 'Oak Hall', 'Onancock', 'Onley', 'Oyster', 'Oakwood',
           'Oceana', 'Orgas', 'Ottawa', 'Orma', 'Ona', 'Omar', 'Odd', 'Orlando', 'Osage', 'Old Fields', 'Onego',
           'Oak City', 'Ocracoke', 'Oakboro', 'Olivia', 'Orrum', 'Oak Island', 'Ocean Isle Beach', 'Oriental', 'Olin',
           'Old Fort', 'Olar', 'Okatie', 'Orchard Hill', 'Oakman', 'Oconee', 'Oglethorpe', 'Odum', 'Offerman',
           'Ochlocknee', 'Ocilla', 'Omega', 'Omaha', 'Orange Park', 'O Brien', 'Olustee', 'Ormond Beach', 'Ocklawaha',
           'Orange Springs', 'Orange Lake', 'Otter Creek', 'Oviedo', 'Orange City', 'Osteen', 'Opa Locka', 'Ochopee',
           'Osprey', 'Ocala', 'Ozona', 'Oldsmar', 'Ocoee', 'Okahumpka', 'Okeechobee', 'Odenville', 'Owens Cross Roads',
           'Ohatchee', 'Ozark', 'Opp', 'Orange Beach', 'Orrville', 'Opelika', 'Old Hickory', 'Only', 'Orlinda',
           'Ooltewah', 'Oliver Springs', 'Obion', 'Olivehill', 'Olive Branch', 'Okolona', 'Ovett', 'Ocean Springs',
           'Oak Vale', 'Osyka', 'Olympia', 'Owenton', 'Owingsville', 'Olive Hill', 'Oil Springs', 'Ophir', 'Oak Grove',
           'Olmstead', 'Owensboro', 'Olaton', 'Ostrander', 'Oak Harbor', 'Oregon', 'Old Washington', 'Oberlin',
           'Olmsted Falls', 'Oceola', 'Okeana', 'Oregonia', 'Overpeck', 'Owensville', 'Osgood', 'Otway', 'Ohio City',
           'Ottoville', 'Orestes', 'Ossian', 'Oakford', 'Onward', 'Ora', 'Oldenburg', 'Otisco', 'Oolitic', 'Owensburg',
           'Oaktown', 'Odon', 'Otwell', 'Oakland City', 'Otterbein', 'Oak Park', 'Ortonville', 'Otter Lake', 'Oakley',
           'Omer', 'Oscoda', 'Owendale', 'Okemos', 'Owosso', 'Olivet', 'Oshtemo', 'Otsego', 'Onondaga', 'Onsted',
           'Osseo', 'Ottawa Lake', 'Old Mission', 'Omena', 'Onekama', 'Oden', 'Onaway', 'Ossineke', 'Ontonagon',
           'Ogden', 'Otley', 'Orchard', 'Otho', 'Ottosen', 'Oelwein', 'Oran', 'Onawa', 'Oto', 'Oyens', 'Ocheyedan',
           'Okoboji', 'Odebolt', 'Onslow', 'Oxford Junction', 'Ottumwa', 'Ollie', 'Oskaloosa', 'Olds', 'Oconomowoc',
           'Okauchee', 'Oostburg', 'Oak Creek', 'Orfordville', 'Oconto', 'Oconto Falls', 'Ogema', 'Owen', 'Onalaska',
           'Odanah', 'Ojibwa', 'Oshkosh', 'Omro', 'Owatonna', 'Orr', 'Oronoco', 'Odin', 'Okabena', 'Ormsby', 'Ogilvie',
           'Onamia', 'Osakis', 'Ottertail', 'Outing', 'Oklee', 'Oslo', 'Oldham', 'Ortley', 'Oacoma', 'Onaka', 'Okaton',
           'Okreek', 'Onida', 'Oelrichs', 'Oglala', 'Oral', 'Owanka', 'Oriska', 'Osnabrock', 'Oberon', 'Oakes', 'Otter',
           'Opheim', 'Outlook', 'Olive', 'Oilmont', 'Ovando', 'Oak Forest', 'Oak Lawn', 'Odell', 'Olympia Fields',
           'Orland Park', 'Oak Brook', 'Onarga', 'Orion', 'Osco', 'Oglesby', 'Ohio', 'Ophiem', 'Oquawka', 'Ohlman',
           'O Fallon', 'Okawville', 'Oblong', 'Oreana', 'Owaneco', 'Opdyke', 'Olmsted', 'Oraville', 'Old Monroe',
           'Old Appleton', 'Oxly', 'Orrick', 'Osborn', 'Oronogo', 'Osage Beach', 'Otterville', 'Oldfield', 'Olathe',
           'Osawatomie', 'Ozawkie', 'OP', 'Overland Park', 'Oketo', 'Olsburg', 'Onaga', 'Osage City', 'Overbrook',
           'Opolis', 'Olpe', 'Osborne', 'Offerle', 'Olmitz', 'Ogallah', 'Offutt A F B', 'Ohiowa', 'Otoe', 'Ong',
           'Oneill', 'Osmond', 'Ord', 'Overton', 'Oak', 'Ogallala', 'Opelousas', 'Oscar', 'Olla', 'Ozan', 'O Kean',
           'Oil Trough', 'Onia', 'Oark', 'Ola', 'Ozone', 'OKC', 'Oklahoma City', 'Okarche', 'Okeene', 'Ochelata',
           'Oilton', 'Oologah', 'Owasso', 'Okay', 'Okmulgee', 'Oktaha', 'Okemah', 'Ore City', 'Oklaunion', 'Olden',
           'Old Ocean', 'Orangefield', 'Odem', 'Orange Grove', 'Olmito', 'Ottine', 'Olton', 'Odonnell', 'Old Glory',
           'Ovalo', 'Orla', 'Ordway', 'Olney Springs', 'Ouray', 'Opal', 'Orofino', 'Osburn', 'Orem', 'Orderville',
           'Oracle', 'Overgaard', 'Oatman', 'Ojo Caliente', 'Ohkay Owingeh', 'Ocate', 'Ojo Feliz', 'Organ', 'Orogrande',
           'Orovada', 'Owyhee', 'Ocotillo', 'Oro Grande', 'Oak View', 'Ojai', 'Oxnard', 'Onyx', 'Oceano', 'Olancha',
           'O Neals', 'Orange Cove', 'Orosi', 'Orinda', 'Olema', 'Occidental', 'Orick', 'Orangevale', 'Olivehurst',
           'Oregon House', 'Oroville', 'Oak Run', 'Obrien', 'Old Station', 'Olympic Valley', 'Ookala', 'Oregon City',
           'Otter Rock', 'Oakridge', 'Olga', 'Orcas',
           'Olalla', 'Orting', 'Ocean Shores', 'Oysterville', 'Okanogan', 'Omak', 'Orondo', 'Otis Orchards',
           'Oakesdale', 'Othello', 'Old Harbor', 'Ouzinkie']
PCities = ['Penuelas', 'Ponce', 'Palmer', 'Patillas', 'Puerto Real', 'Punta Santiago', 'Plainfield', 'Pittsfield',
           'Petersham', 'Pepperell', 'Princeton',
           'Paxton', 'Pinehurst', 'Peabody', 'Prides Crossing', 'Pembroke', 'Plymouth', 'Plympton', 'Pocasset',
           'Provincetown', 'Plainville', 'Pascoag', 'Pawtucket', 'Portsmouth', 'Prudence Island', 'Peace Dale',
           'Providence', 'Pelham', 'Peterborough', 'Pittsburg', 'Piermont', 'Pike', 'Plaistow', 'Parsonsfield',
           'Porter', 'Pownal', 'Portland', 'Peaks Island', 'Paris', 'Poland', 'Peru', 'Palermo', 'Passadumkeag',
           'Penobscot', 'Pemaquid', 'Phippsburg', 'Perry', 'Prospect Harbor', 'Patten', 'Perham', 'Portage',
           'Presque Isle', 'Port Clyde', 'Palmyra', 'Phillips', 'Post Mills', 'Perkinsville', 'Proctorsville', 'Putney',
           'Pawlet', 'Pittsford', 'Poultney', 'Proctor', 'Passumpsic', 'Peacham', 'Pine Meadow', 'Poquonock', 'Pomfret',
           'Pomfret Center', 'Putnam', 'Preston', 'Pawcatuck', 'Plantsville', 'Prospect', 'Pequabuck', 'Parsippany',
           'Passaic', 'Pine Brook', 'Port Reading', 'Pequannock', 'Pompton Lakes', 'Pompton Plains', 'Paterson',
           'Palisades Park', 'Paramus', 'Park Ridge', 'Port Monmouth', 'Picatinny Arsenal', 'Port Murray', 'Peapack',
           'Pluckemin', 'Pottersville', 'Paulsboro', 'Pedricktown', 'Pemberton', 'Penns Grove', 'Pennsville', 'Pitman',
           'Pennsauken', 'Pleasantville', 'Pomona', 'Port Republic', 'Port Elizabeth', 'Port Norris', 'Pennington',
           'Plainsboro', 'Princeton Junction', 'Pine Beach', 'Point Pleasant Beach', 'Piscataway', 'Parlin',
           'Perth Amboy', 'Phillipsburg', 'Pittstown', 'Peekskill', 'Port Chester', 'Pound Ridge', 'Purchase', 'Purdys',
           'Putnam Valley', 'Palisades', 'Pearl River', 'Pine Island', 'Port Washington', 'Point Lookout', 'Patchogue',
           'Port Jefferson Station', 'P J S', 'PJS', 'Port Jefferson', 'Plainview', 'Peconic', 'Pattersonville',
           'Petersburg', 'Piseco', 'Poestenkill', 'Palenville', 'Phoenicia', 'Pine Hill', 'Port Ewen', 'Prattsville',
           'Preston Hollow', 'Purling', 'Patterson', 'Pawling', 'Philmont', 'Pine Bush', 'Pine Plains', 'Plattekill',
           'Pleasant Valley', 'Poughquag', 'Poughkeepsie', 'Parksville', 'Phillipsport', 'Pond Eddy', 'Port Jervis',
           'Paradox', 'Porter Corners', 'Putnam Station', 'Plattsburgh', 'Paul Smiths', 'Piercefield', 'Port Henry',
           'Port Kent', 'Parish', 'Pennellville', 'Peterboro', 'Phoenix', 'Pitcher', 'Pompey', 'Poplar Ridge',
           'Port Byron', 'Preble', 'Pulaski', 'Palatine Bridge', 'Port Leyden', 'Parishville', 'Philadelphia',
           'Pierrepont Manor', 'Plessis', 'Potsdam', 'Pyrites', 'Port Crane', 'Portlandville', 'Perrysburg', 'Pavilion',
           'Penfield', 'Penn Yan', 'Phelps', 'Piffard', 'Portageville', 'Port Gibson', 'Pultneyville', 'Panama',
           'Portville', 'Painted Post', 'Pine City', 'Pine Valley', 'Prattsburgh', 'Pulteney', 'Pricedale', 'Pitcairn',
           'Presto', 'Pittsburgh', 'Prosperity', 'Perryopolis', 'Point Marion', 'Penn', 'Pleasant Unity', 'Penn Run',
           'Punxsutawney', 'Parkhill', 'Parker', 'Petrolia', 'Portersville', 'Plumville', 'Polk', 'Patton',
           'Port Allegany', 'Pennsylvania Furnace', 'Philipsburg', 'Pine Grove Mills', 'Port Matilda', 'Pottersdale',
           'Pillow', 'Port Royal', 'Pleasant Hall', 'Porters Sideling', 'Peach Glen', 'Paradise', 'Peach Bottom',
           'Penryn', 'Pequea', 'Picture Rocks', 'Paxinos', 'Paxtonville', 'Penns Creek', 'Port Trevorton',
           'Potts Grove', 'Pottsville', 'Pine Grove', 'Port Carbon', 'Palm', 'Palmerton', 'Pen Argyl', 'Pennsburg',
           'Perkiomenville', 'Parryville', 'Pocono Summit', 'Pocono Lake', 'Pocono Lake Preserve', 'Pocono Manor',
           'Pocono Pines', 'Paupack', 'Peckville', 'Pleasant Mount', 'Poyntelle', 'Preston Park', 'Prompton',
           'Pittston', 'Penns Park', 'Perkasie', 'Pineville', 'Pipersville', 'Plumsteadville', 'Point Pleasant',
           'Prospect Park', 'Paoli', 'Parkesburg', 'Pocopson', 'Pomeroy', 'Parker Ford', 'Phoenixville',
           'Plymouth Meeting', 'Pottstown', 'Pine Forge', 'Port Clinton', 'Port Penn', 'Paeonian Springs', 'Philomont',
           'Purcellville', 'Park Hall', 'Patuxent River', 'Piney Point', 'Port Tobacco', 'Prince Frederick',
           'Poolesville', 'Potomac', 'Parkton', 'Pasadena', 'Perry Hall', 'Perryman', 'Pylesville', 'Pikesville',
           'Parkville', 'Pinto', 'Price', 'Point Of Rocks', 'Parsonsburg', 'Pittsville', 'Pocomoke City', 'Powellville',
           'Princess Anne', 'Perry Point', 'Perryville', 'Port Deposit', 'Partlow', 'Pratts', 'Penn Laird',
           'Piney River', 'Port Haywood', 'Powhatan', 'Providence Forge', 'Painter', 'Parksley', 'Pungoteague',
           'Poquoson', 'Prince George', 'Pamplin', 'Phenix', 'Paint Bank', 'Parrott', 'Patrick Springs', 'Pearisburg',
           'Penhook', 'Pilot', 'Pennington Gap', 'Pound', 'Pilgrims Knob', 'Pocahontas', 'Pounding Mill', 'Pageton',
           'Panther', 'Paynesville', 'Premier', 'Pence Springs', 'Peterstown', 'Page', 'Peytona', 'Pinch', 'Poca',
           'Pond Gap', 'Powellton', 'Pratt', 'Procious', 'Paw Paw', 'Points', 'Pecks Mill', 'Prichard', 'Peach Creek',
           'Pax', 'Piney View', 'Prince', 'Princewick', 'Pipestem', 'Parkersburg', 'Paden City', 'Palestine',
           'Petroleum', 'Porters Falls', 'Pickens', 'Parsons', 'Pennsboro', 'Philippi', 'Pullman', 'Pentress',
           'Pursglove', 'Pool', 'Piedmont', 'Purgitsville', 'Pfafftown', 'Pilot Mountain', 'Pine Hall', 'Pinnacle',
           'Pittsboro', 'Pleasant Garden', 'Prospect Hill', 'Pine Level', 'Pantego', 'Parmele', 'Pendleton',
           'Pikeville', 'Pinetops', 'Pinetown', 'Pleasant Hill', 'Potecasi', 'Point Harbor', 'Poplar Branch',
           'Powells Point', 'Powellsville', 'Paw Creek', 'Peachland', 'Polkton', 'Polkville', 'Pope Army Airfield',
           'Pinebluff', 'Proctorville', 'Pink Hill', 'Pollocksville', 'Pineola', 'Piney Creek', 'Plumtree', 'Purlear',
           'Penland', 'Penrose', 'Pisgah Forest', 'Peak', 'Pelion', 'Pinewood', 'Pomaria', 'Pacolet', 'Pacolet Mills',
           'Pauline', 'Pinopolis', 'Pamplico', 'Patrick', 'Pawleys Island', 'Pelzer', 'Pageland', 'Plum Branch',
           'Parris Island', 'Pineland', 'Porterdale', 'Pine Lake', 'Powder Springs', 'Palmetto', 'Peachtree City',
           'Portal', 'Pendergrass', 'Perkins', 'Pineview', 'Pitts', 'Pooler', 'Port Wentworth', 'Pearson', 'Pavo',
           'Plains', 'Poulan', 'Pine Mountain', 'Pine Mountain Valley', 'Ponte Vedra Beach', 'Penney Farms',
           'Ponte Vedra', 'Port Orange', 'Palm Coast', 'Palatka', 'Pierson', 'Pomona Park', 'Putnam Hall', 'Panacea',
           'Pinetta', 'Panama City', 'Panama City Beach', 'Ponce De Leon', 'Port Saint Joe', 'Pensacola', 'Paisley',
           'Palm Bay', 'Patrick AFB', 'Pembroke Pines', 'Pompano Beach', 'Plantation', 'Palm Beach Gardens', 'Pahokee',
           'Palm Beach', 'Plant City', 'Pinellas Park', 'Polk City', 'Palmdale', 'Placida', 'Port Charlotte',
           'Punta Gorda', 'Parrish', 'Port Richey', 'Palm Harbor', 'Port Saint Lucie', 'Palm City', 'Port Salerno',
           'Palmerdale', 'Pell City', 'Pinson', 'Pleasant Grove', 'Panola', 'Peterson', 'Phil Campbell', 'Paint Rock',
           'Pisgah', 'Perote', 'Petrey', 'Pike Road', 'Prattville', 'Pansey', 'Pinckard', 'Perdue Hill', 'Peterman',
           'Perdido', 'Point Clear', 'Plantersville', 'Pine Apple', 'Phenix City', 'Pittsview', 'Pegram',
           'Pleasant Shade', 'Pleasant View', 'Piney Flats', 'Parrottsville', 'Petros', 'Pioneer', 'Powell', 'Pruden',
           'Pigeon Forge', 'Palmersville', 'Puryear', 'Pickwick Dam', 'Primm Springs', 'Pall Mall', 'Pope',
           'Potts Camp', 'Parchman', 'Pace', 'Panther Burn', 'Pontotoc', 'Philipp', 'Pattison', 'Pelahatchie',
           'Piney Woods', 'Pinola', 'Puckett', 'Pearl', 'Pachuta', 'Paulding', 'Porterville', 'Petal', 'Picayune',
           'Poplarville', 'Prentiss', 'Purvis', 'Pascagoula', 'Pass Christian', 'Pearlington', 'Perkinston', 'Pheba',
           'Prairie', 'Pewee Valley', 'Pleasureville', 'Payneville', 'Perry Park', 'Paint Lick', 'Partridge',
           'Pathfork', 'Plummers Landing', 'Paintsville', 'Pilgrim', 'Pine Ridge', 'Phyllis', 'Pinsonfork',
           'Prestonsburg', 'Printer', 'Pine Top', 'Pippa Passes', 'Premium', 'Paducah', 'Park City', 'Pellville',
           'Philpot', 'Powderly', 'Poole', 'Parkers Lake', 'Pine Knot', 'Pataskala', 'Plain City', 'Pickerington',
           'Pemberville', 'Put In Bay', 'Pettisville', 'Philo', 'Pleasant City', 'Piney Fork', 'Powhatan Point',
           'Painesville', 'Parkman', 'Pierpont', 'Peninsula', 'Perrysville', 'Pleasant Plain', 'Port William', 'Piqua',
           'Pitsburg', 'Patriot', 'Pedro', 'Peebles', 'Piketon', 'Pandora', 'Payne', 'Paragon', 'Putnamville',
           'Pierceton', 'Pleasant Lake', 'Pleasant Mills', 'Poneto', 'Pierceville', 'Pekin', 'Paris Crossing',
           'Parker City', 'Pennville', 'Pershing', 'Patricksburg', 'Poseyville', 'Patoka', 'Pimento', 'Prairie Creek',
           'Prairieton', 'Pine Village', 'Port Huron', 'Pleasant Ridge', 'Pinckney', 'Pontiac', 'Palms', 'Peck',
           'Port Austin', 'Port Hope', 'Port Sanilac', 'Pinconning', 'Prudenville', 'Pigeon', 'Prescott', 'Palo',
           'Perrinton', 'Pewamo', 'Pompeii', 'Potterville', 'Plainwell', 'Parma', 'Pentwater', 'Pellston', 'Petoskey',
           'Pickford', 'Pointe Aux Pins', 'Posen', 'Perronville', 'Powers', 'Painesdale', 'Pelkie', 'Panora', 'Paton',
           'Pella', 'Pilot Mound', 'Popejoy', 'Prairie City', 'Prole', 'Plover', 'Paullina', 'Primghar',
           'Pacific Junction', 'Persia', 'Percival', 'Peosta', 'Postville', 'Protivin', 'Prairieburg', 'Parnell',
           'Packwood', 'Plano', 'Promise City', 'Pilot Grove', 'Pewaukee', 'Pell Lake', 'Pleasant Prairie',
           'Powers Lake', 'Plain', 'Prairie Du Sac', 'Patch Grove', 'Platteville', 'Potosi', 'Prairie Du Chien',
           'Packwaukee', 'Pardeeville', 'Poynette', 'Pembine', 'Peshtigo', 'Porterfield', 'Potter', 'Pelican Lake',
           'Phlox', 'Pickerel', 'Port Edwards', 'Park Falls', 'Prentice', 'Pepin', 'Pigeon Falls', 'Plum City',
           'Prairie Farm', 'Poplar', 'Port Wing', 'Pickett', 'Pine River', 'Poy Sippi', 'Plato', 'Prior Lake',
           'Pengilly', 'Pipestone', 'Pennock', 'Prinsburg', 'Parkers Prairie', 'Pease', 'Pierz', 'Palisade',
           'Park Rapids', 'Pequot Lakes', 'Pillager', 'Pelican Rapids', 'Perley', 'Ponsford', 'Ponemah', 'Puposky',
           'Plummer', 'Parcel Return Service', 'PRS', 'Peever', 'Parkston', 'Pickstown', 'Plankinton', 'Platte',
           'Pukwana', 'Pierre', 'Parmelee', 'Philip', 'Presho', 'Pollock', 'Porcupine', 'Pringle', 'Pillsbury',
           'Park River', 'Pembina', 'Pisek', 'Perth', 'Pettibone', 'Pingree', 'Parshall', 'Plaza', 'Pompeys Pillar',
           'Pray', 'Pryor', 'Peerless', 'Plentywood', 'Plevna', 'Powderville', 'Pendroy', 'Power', 'Polaris', 'Pony',
           'Pinesdale', 'Pablo', 'Polson', 'Polebridge', 'Palatine', 'Prospect Heights', 'Plato Center',
           'Palos Heights', 'Palos Park', 'Palos Hills', 'Park Forest', 'Peotone', 'Papineau', 'Pembroke Township',
           'Piper City', 'Pearl City', 'Pecatonica', 'Polo', 'Poplar Grove', 'Preemption', 'Prophetstown',
           'Princeville', 'Peoria', 'Peoria Heights', 'Pesotum', 'Piasa', 'Percy', 'Pierron', 'Pinckneyville',
           'Prairie Du Rocher', 'Paloma', 'Payson', 'Pana', 'Pawnee', 'Pleasant Plains', 'Perks', 'Pacific', 'Pevely',
           'Portage Des Sioux', 'Park Hills', 'Pilot Knob', 'Poplar Bluff', 'Puxico', 'Peculiar', 'Platte City',
           'Pickering', 'Plattsburg', 'Pattonsburg', 'Powersville', 'Purdin', 'Purcell', 'Prairie Home', 'Pierce City',
           'Pleasant Hope', 'Powersite', 'Protem', 'Purdy', 'Peace Valley', 'Paola', 'Pleasanton', 'Prairie Village',
           'Paxico', 'Powhattan', 'Potwin', 'Protection', 'Portis', 'Pawnee Rock', 'Pretty Prairie', 'Palco', 'Penokee',
           'Pfeifer', 'Prairie View', 'Park', 'Papillion', 'Pender', 'Plattsmouth', 'Prague', 'Pawnee City', 'Pickrell',
           'Pleasant Dale', 'Platte Center', 'Primrose', 'Pierce', 'Pilger', 'Ponca', 'Parks', 'Purdum', 'Paradis',
           'Pilottown', 'Pointe A La Hache', 'Port Sulphur', 'Pierre Part', 'Paincourtville', 'Plattenville',
           'Ponchatoula', 'Pine Prairie', 'Port Barre', 'Pitkin', 'Paulina', 'Plaquemine', 'Port Allen', 'Prairieville',
           'Pride', 'Pelican', 'Plain Dealing', 'Plaucheville', 'Provencal', 'Pine Bluff', 'Parkdale', 'Pearcy',
           'Pencil Bluff', 'Pangburn', 'Paron', 'Plumerville', 'Poyen', 'Prim', 'Parkin', 'Paragould', 'Peach Orchard',
           'Piggott', 'Pollard', 'Portia', 'Parthenon', 'Peel', 'Pindall', 'Pyatt', 'Pea Ridge', 'Pettigrew',
           'Prairie Grove', 'Pelsor', 'Pauls Valley', 'Pond Creek', 'Pawhuska', 'Prue', 'Picher', 'Park Hill', 'Peggs',
           'Porum', 'Ponca City', 'Platter', 'Paden', 'Pocola', 'Poteau', 'Pottsboro', 'Prosper', 'Pattonville',
           'Pecan Gap', 'Petty', 'Pickton', 'Point', 'Poynor', 'Pollok', 'Pilot Point', 'Ponder', 'Paluxy',
           'Palo Pinto', 'Peaster', 'Perrin', 'Poolville', 'Purmela', 'Penelope', 'Prairie Hill', 'Purdon', 'Priddy',
           'Pointblank', 'Palacios', 'Pledger', 'Pearland', 'Port Arthur', 'Port Bolivar', 'Port Neches', 'Placedo',
           'Point Comfort', 'Port Lavaca', 'Port O Connor', 'Pearsall', 'Peggy', 'Pipe Creek', 'Poteet', 'Panna Maria',
           'Pettus', 'Poth', 'Port Aransas', 'Premont', 'Penitas', 'Pharr', 'Port Isabel', 'Progreso', 'Port Mansfield',
           'Paige', 'Pflugerville', 'Prairie Lea', 'Plum', 'Pampa', 'Panhandle', 'Perryton', 'Pep', 'Post', 'Pecos',
           'Penwell', 'Pyote', 'Presidio', 'Palmer Lake', 'Pine', 'Pinecliffe', 'Padroni', 'Peetz', 'Peyton', 'Pueblo',
           'Pritchett', 'Pagosa Springs', 'Poncha Springs', 'Powderhorn', 'Paonia', 'Placerville', 'Parachute',
           'Pine Bluffs', 'Pavillion', 'Powder River', 'Pinedale', 'Pocatello', 'Paul', 'Picabo', 'Payette', 'Ponderay',
           'Porthill', 'Post Falls', 'Potlatch', 'Priest River', 'Peoa', 'Park Valley', 'Provo', 'Panguitch',
           'Paragonah', 'Parowan', 'Picacho', 'Paradise Valley', 'Palo Verde', 'Poston', 'Peridot', 'Pima', 'Patagonia',
           'Pearce', 'Pirtleville', 'Pomerene', 'Pinetop', 'Petrified Forest Natl Pk', 'Polacca', 'Prescott Valley',
           'Paulden', 'Peach Springs', 'Pinon', 'Pueblo Of Acoma', 'Paguate', 'Pena Blanca', 'Peralta', 'Placitas',
           'Ponderosa', 'Prewitt', 'Pinehill', 'Penasco', 'Petaca', 'Pie Town', 'Polvadera', 'Playas', 'Pinos Altos',
           'Portales', 'Pahrump', 'Panaca', 'Pioche', 'Playa Vista', 'Pacific Palisades', 'Palos Verdes Peninsula',
           'Playa Del Rey', 'Pico Rivera', 'Paramount', 'Porter Ranch', 'Pacoima', 'Panorama City', 'Potrero', 'Pala',
           'Palomar Mountain', 'Pauma Valley', 'Poway', 'Palm Desert', 'Palm Springs', 'Parker Dam', 'Pioneertown',
           'Phelan', 'Pinon Hills', 'Perris', 'Placentia', 'Piru', 'Port Hueneme', 'Point Mugu Nawc',
           'Port Hueneme Cbc Base', 'Pine Mountain Club', 'Pixley', 'Posey', 'Paso Robles', 'Pismo Beach',
           'Pearblossom', 'Parlier', 'Piedra', 'Prather', 'Pacific Grove', 'Pebble Beach', 'Portola Valley', 'Pacifica',
           'Pescadero', 'Palo Alto', 'Pinole', 'Pope Valley', 'Port Costa', 'Penngrove', 'Petaluma',
           'Point Reyes Station', 'Paicines', 'Pinecrest', 'Planada', 'Point Arena', 'Potter Valley', 'Phillipsville',
           'Piercy', 'Pilot Hill', 'Pollock Pines', 'Penn Valley', 'Palo Cedro', 'Paskenta', 'Paynes Creek', 'Platina',
           'Proberta', 'Portola', 'Paauilo', 'Pahala', 'Pahoa', 'Paia', 'Papaaloa', 'Papaikou', 'Pepeekeo', 'Puunene',
           'Pukalani', 'Pago Pago', 'Palau', 'Pohnpei', 'Pacific City', 'Philomath', 'Port Orford', 'Plush',
           'Powell Butte', 'Prineville', 'Pilot Rock', 'Point Roberts', 'Port Hadlock', 'Port Angeles', 'Port Gamble',
           'Port Ludlow', 'Port Orchard', 'Port Townsend', 'Poulsbo', 'Puyallup', 'Paradise Inn', 'Pacific Beach',
           'Pe Ell', 'Pateros', 'Peshastin', 'Palouse', 'Pasco', 'Prosser', 'Port Heiden',
           'Port Lions', 'Pedro Bay', 'Pilot Station', 'Platinum', 'Port Alsworth', 'Prudhoe Bay', 'Point Lay',
           'Point Hope', 'Port Alexander', 'Point Baker']
QCities = ['Quebradillas', 'Quincy', 'Quechee', 'Quinebaug', 'Quaker Hill', 'Quinton', 'Quakertown', 'Queens Village',
           'Quogue', 'Quaker Street', 'Queensbury',
           'Quecreek', 'Queen', 'Quentin', 'Quarryville', 'Quakake', 'Queen Anne', 'Queenstown', 'Quantico',
           'Quicksburg', 'Quinque', 'Quinby', 'Quinwood', 'QVC',
           'Quitman', 'Quebeck', 'Quaker City', 'Quinnesec', 'Quimby', 'Quasqueton', 'Quinn', 'Queen City', 'Qulin',
           'Quenemo', 'Quinter', 'Quapaw', 'Quinlan',
           'Quemado', 'Quail', 'Quanah', 'Quitaque', 'Queen Creek', 'Quartzsite', 'Questa', 'Quay', 'Quail Valley',
           'Quilcene', 'Quinault', 'Quinhagak']
RCities = ['Rosario', 'Rincon', 'Roosevelt Roads', 'Rio Blanco', 'Rio Grande', 'Russell', 'Richmond', 'Rowe',
           'Royalston', 'Rochdale', 'Rutland',
           'Reading', 'Rockport', 'Rowley', 'Roxbury', 'Roxbury Crossing', 'Roslindale', 'Readville', 'Revere',
           'Randolph', 'Rockland', 'Raynham',
           'Raynham Center', 'Rehoboth', 'Rochester', 'Rockville', 'Riverside', 'Rumford', 'Raymond', 'Rumney',
           'Rindge', 'Rollinsford', 'Rye', 'Rye Beach', 'Readfield', 'Rockwood', 'Round Pond', 'Robbinston', 'Rangeley',
           'Randolph Center', 'Readsboro', 'Richford', 'Ripton', 'Rupert', 'Riverton', 'Rocky Hill', 'Rogers',
           'Rockfall', 'Redding Center', 'Redding Ridge', 'Ridgefield', 'Redding', 'Rahway', 'Roseland', 'Rutherford',
           'Roselle', 'Roselle Park', 'Ramsey', 'Ridgewood', 'Ringwood', 'Riverdale', 'Ridgefield Park', 'River Edge',
           'Rochelle Park', 'Red Bank', 'Rumson', 'Rockaway', 'Rancocas', 'Richwood', 'Runnemede', 'Richland',
           'Rosenhayn', 'Ringoes', 'Roebling', 'Roosevelt', 'Rosemont', 'Raritan', 'Readington', 'Rego Park',
           'Richmond Hill', 'Rosedale', 'Rockville Centre', 'RVC', 'Roslyn', 'Roslyn Heights', 'Rockaway Park',
           'Rocky Point', 'Ronkonkoma', 'Riverhead', 'Remsenburg', 'Ridge', 'Ravena', 'Rensselaer', 'Rensselaerville',
           'Rexford', 'Richmondville', 'Rotterdam Junction', 'Round Lake', 'Rifton', 'Rosendale', 'Round Top', 'Ruby',
           'Red Hook', 'Rhinebeck', 'Rhinecliff', 'Rock Tavern', 'Rock Hill', 'Roscoe', 'Riparius', 'Rock City Falls',
           'Rainbow Lake', 'Ray Brook', 'Redford', 'Rouses Point', 'Red Creek', 'Raquette Lake', 'Redfield', 'Remsen',
           'Richfield Springs', 'Rome', 'Roseboom', 'Raymondville', 'Redwood', 'Rensselaer Falls', 'Richville',
           'Rodman', 'Rooseveltown', 'Ransomville', 'Retsof', 'Romulus', 'Rose', 'Rush', 'Rushville', 'Richburg',
           'Ripley', 'Rushford', 'Reading Center', 'Rexville', 'Rock Stream', 'Rural Ridge', 'Russellton',
           'Rices Landing', 'Richeyville', 'Rogersville', 'Republic', 'Ronco', 'Rector', 'Rillton', 'Ruffs Dale',
           'Ringgold', 'Rochester Mills', 'Rossiter', 'Reynoldsville', 'Ridgway', 'Rockton', 'Revloc', 'Robinson',
           'Renfrew', 'Rimersburg', 'Rural Valley', 'Reno', 'Rouseville', 'Riceville', 'Ramey', 'Riddlesburg',
           'Roaring Spring', 'Robertsdale', 'Rew', 'Rixford', 'Roulette', 'Rebersburg', 'Reedsville', 'Rexmont',
           'Richfield', 'Rockhill Furnace', 'Rouzerville', 'Railroad', 'Red Lion', 'Rossville', 'Reamstown', 'Refton',
           'Reinholds', 'Rheems', 'Ronks', 'Ralston', 'Renovo', 'Roaring Branch', 'Rebuck', 'Ravine', 'Ringtown',
           'Red Hill', 'Riegelsville', 'Rock Glen', 'Reeders', 'Rowland', 'Ransom', 'Richboro', 'Richlandtown',
           'Rushland', 'Ridley Park', 'Royersford', 'Rehrersburg', 'Robesonia', 'Rehoboth Beach', 'Rectortown',
           'Round Hill', 'Reston', 'Rock Point', 'Randallstown', 'Reisterstown', 'Riderwood', 'Riva', 'Rawlings',
           'Rhodesdale', 'Ridgely', 'Rock Hall', 'Royal Oak', 'Rocky Ridge', 'Rohrersville', 'Rehobeth', 'Rising Sun',
           'Rappahannock Academy', 'Reedville', 'Rhoadesville', 'Rollins Fork', 'Ruther Glen', 'Rileyville', 'Radiant',
           'Rapidan', 'Remington', 'Reva', 'Richardsville', 'Rixeyville', 'Rochelle', 'Ruckersville', 'Ruthville',
           'Rescue', 'Red House', 'Red Oak', 'Rice', 'Roanoke', 'Radford', 'Rich Creek', 'Ridgeway', 'Riner',
           'Ripplemead', 'Rocky Mount', 'Rose Hill', 'Rocky Gap', 'Rural Retreat', 'Raphine', 'Rockbridge Baths',
           'Rustburg', 'Raven', 'Red Ash', 'Richlands', 'Rock', 'Raysal', 'Rock View', 'Roderfield', 'Renick',
           'Ronceverte', 'Racine', 'Ridgeview', 'Robson', 'Rock Creek', 'Reedy', 'Ranson', 'Rippon', 'Ranger',
           'Ragland', 'Rawl', 'Red Jacket', 'Raleigh', 'Ravencliff', 'Rhodell', 'Rainelle', 'Ravenswood', 'Reader',
           'Rock Cave', 'Rowlesburg', 'Rachel', 'Rivesville', 'Ridgeley', 'Rio', 'Romney', 'Rural Hall', 'Ramseur',
           'Randleman', 'Reidsville', 'Robbins', 'Ruffin', 'Rolesville', 'Rougemont', 'Roxboro', 'RTP',
           'Research Triangle Park', 'Rich Square', 'Roanoke Rapids', 'Robersonville', 'Roxobel', 'Rodanthe', 'Roduco',
           'Roper', 'Rockwell', 'Rutherfordton', 'Raeford', 'Red Springs', 'Rex', 'Rockingham', 'Roseboro',
           'Riegelwood', 'Rhodhiss', 'Roaring Gap', 'Roaring River', 'Ronda', 'Rutherford College', 'Ridgecrest',
           'Robbinsville', 'Rosman', 'Rembert', 'Ridge Spring', 'Rion', 'Rowesville', 'Reidville', 'Roebuck', 'Ravenel',
           'Reevesville', 'Ridgeville', 'Round O', 'Russellville', 'Rains', 'Ridgeland', 'Redan', 'Roswell', 'Rockmart',
           'Roopville', 'Rydal', 'Register', 'Rockledge', 'Rocky Ford', 'Rabun Gap', 'Rayle', 'Royston', 'Rutledge',
           'Resaca', 'Rising Fawn', 'Rock Spring', 'Rocky Face', 'Rentz', 'Reynolds', 'Rhine', 'Roberta', 'Riceboro',
           'Ray City', 'Rebecca', 'Raiford', 'Rosemary Beach', 'Reddick', 'Royal Palm Beach', 'Riverview', 'Ruskin',
           'River Ranch', 'Rotonda West', 'Remlap', 'Rockford', 'Ralph', 'Reform', 'Red Bay', 'Ryland', 'Rainbow City',
           'RBC', 'Rainsville', 'Ramer', 'Ranburne', 'Range', 'Red Level', 'Repton', 'River Falls', 'Readyville',
           'Red Boiling Springs', 'Riddleton', 'Ridgetop', 'Rockvale', 'Reliance', 'Roan Mountain', 'Rugby', 'Rives',
           'Reagan', 'Rickman', 'Rock Island', 'Red Banks', 'Robinsonville', 'Rena Lara', 'Ruleville', 'Rienzi',
           'Rolling Fork', 'Richton', 'Roxie', 'Ruth', 'Raywick', 'Radcliff', 'Rhodelia', 'Rineyville', 'Ravenna',
           'Renfro Valley', 'Rockholds', 'Roark', 'River', 'Ricetown', 'Rousseau', 'Rowdy', 'Royalton', 'Raccoon',
           'Regina', 'Robinson Creek', 'Rockhouse', 'Redfox', 'Roxana', 'Rockfield', 'Roundhill', 'Reynolds Station',
           'Rosine', 'Rumsey', 'Reed', 'Robards', 'Revelo', 'Russell Springs', 'Radnor', 'Reynoldsburg', 'Rosewood',
           'Rockbridge', 'Roundhead', 'Rushsylvania', 'Russells Point', 'Risingsun', 'Rossford', 'Rudolph',
           'Ridgeville Corners', 'Roseville', 'Rayland', 'Rocky River', 'Rittman', 'Rootstown', 'Robertsville', 'Ross',
           'Reesville', 'Rossburg', 'Russia', 'Rarden', 'Ray', 'Richmond Dale', 'Rock Camp', 'Rawson', 'Reelsville',
           'Roachdale', 'Rolling Prairie', 'Roselawn', 'Rome City', 'Roann', 'Royal Center', 'Russiaville', 'Redkey',
           'Ragsdale', 'Riley', 'Romeo', 'River Rouge', 'Rhodes', 'Roscommon', 'Rose City', 'Reese', 'Rosebush', 'Riga',
           'Rives Junction', 'Remus', 'Rodney', 'Rothbury', 'Rapid City', 'Reed City', 'Rogers City', 'Rudyard',
           'Rumely', 'Rapid River', 'Ramsay', 'Radcliffe', 'Randall', 'Reasnor', 'Rippey', 'Roland', 'Runnells', 'Rake',
           'Rock Falls', 'Rowan', 'Rudd', 'Rembrandt', 'Renwick', 'Ringsted', 'Rockwell City', 'Rolfe', 'Readlyn',
           'Reinbeck', 'Rock Rapids', 'Rock Valley', 'Royal', 'Ruthven', 'Ricketts', 'Randalia', 'Robins', 'Ryan',
           'Random Lake', 'Rubicon', 'Reeseville', 'Rewey', 'Richland Center', 'Reedsburg', 'Rock Springs', 'Roberts',
           'Rib Lake', 'Ringle', 'Rosholt', 'Rothschild', 'Rhinelander', 'Readstown', 'Radisson', 'Rice Lake',
           'Redgranite', 'Ripon', 'Red Wing', 'Rosemount', 'Rush City', 'Reads Landing', 'Rollingstone', 'Rose Creek',
           'Rushmore', 'Ruthton', 'Redwood Falls', 'Renville', 'Rochert', 'Rothsay', 'Ranier', 'Redby', 'Redlake',
           'Remer', 'Red Lake Falls', 'Roseau', 'Ramona', 'Renner', 'Revillo', 'Ree Heights', 'Rockham', 'Rosebud',
           'Redig', 'Rocklake', 'Rolette', 'Rolla', 'Regan', 'Reeder', 'Regent', 'Rhame', 'Richardton', 'Roseglen',
           'Ruso', 'Ryder', 'Rapelje', 'Red Lodge', 'Reed Point', 'Roundup', 'Ryegate', 'Redstone', 'Reserve', 'Richey',
           'Raynesford', 'Roy', 'Radersburg', 'Ringling', 'Ravalli', 'Ronan', 'Rollins', 'Rolling Meadows',
           'River Grove', 'River Forest', 'Romeoville', 'Richton Park', 'Rankin', 'Ridott', 'Rock City', 'Rapids City',
           'Rantoul', 'Ridge Farm', 'Redmon', 'Roodhouse', 'Rosamond', 'Red Bud', 'Renault', 'Radom', 'Richview',
           'Rinard', 'Rosiclare', 'Richwoods', 'Risco', 'Rombauer', 'Raymore', 'Rayville', 'Ravenwood', 'Rea',
           'Rock Port', 'Rothville', 'Richards', 'Rich Hill', 'Reeds', 'Rocky Comfort', 'Rhineland', 'Rocheport',
           'Rush Hill', 'Roby', 'Reeds Spring', 'Ridgedale', 'Rockaway Beach', 'Rueter', 'Roach', 'Rosalia', 'Rozel',
           'Rush Center', 'Rosalie', 'Roca', 'Rulo', 'Rising City', 'Ragan', 'Red Cloud', 'Republican City', 'Raceland',
           'Robert', 'Rayne', 'Reddell', 'Ragley', 'Reeves', 'Rosepine', 'Rougon', 'Rodessa', 'Ruston', 'Rhinehart',
           'Robeline', 'Rison', 'Rohwer', 'Rosston', 'Reydell', 'Roe', 'Romance', 'Rose Bud', 'Rivervale', 'Ravenden',
           'Ravenden Springs', 'Reyno', 'Rosie', 'Rover', 'Ratcliff', 'Rudy', 'Rush Springs', 'Ravia', 'Ratliff City',
           'Randlett', 'Reydon', 'Rocky', 'Redbird', 'Rentiesville', 'Rattan', 'Red Rock', 'Ringold', 'Rufe', 'Roff',
           'Rowlett', 'Rockwall', 'Richardson', 'Rosser', 'Royse City', 'Roxton', 'Redwater', 'Reklaw', 'Rusk',
           'Rainbow', 'Rhome', 'Rio Vista', 'Rising Star', 'Rockdale', 'Riesel', 'Richland Springs', 'Rowena',
           'Robert Lee', 'Romayor', 'Rosenberg', 'Raywood', 'Rosharon', 'Roans Prairie', 'Rio Medina', 'Randolph AFB',
           'Runge', 'Realitos', 'Refugio', 'Riviera', 'Robstown', 'Rio Grande City', 'Rio Hondo', 'Roma',
           'Round Mountain', 'Round Rock', 'RMX', 'Rio Frio', 'Rocksprings', 'Rosanky', 'Roaring Springs', 'Ralls',
           'Ropesville', 'Ransom Canyon', 'Rotan', 'Rule', 'Rand', 'Rollinsville', 'Red Feather Lakes', 'Roggen',
           'Ramah', 'Rico', 'Redvale', 'Rangely', 'Red Cliff', 'Rifle', 'Rock River', 'Rawlins', 'Recluse', 'Rozet',
           'Ranchester', 'Robertson', 'Rogerson', 'Rexburg', 'Rigby', 'Ririe', 'Reubens', 'Riggins', 'Rathdrum',
           'Rush Valley', 'Redmond', 'Rio Verde', 'Roll', 'Rio Rico', 'Rillito', 'Rimrock', 'Red Valley', 'Rio Rancho',
           'Ranchos De Taos', 'Red River', 'Ribera', 'Raton', 'Rociada', 'Radium Springs', 'Redrock', 'Rodeo',
           'Ruidoso', 'Ruidoso Downs', 'Ruby Valley', 'Rancho Palos Verdes', 'Redondo Beach', 'Reseda',
           'Rancho Cucamonga', 'Rowland Heights', 'Rosemead', 'Ranchita', 'Rancho Santa Fe', 'Rancho Mirage',
           'Redlands', 'Rialto', 'Rimforest', 'Running Springs', 'RSM', 'Rancho Santa Margarita', 'Richgrove',
           'Randsburg', 'Red Mountain', 'Raisin City', 'Reedley', 'Redwood City', 'Rohnert Park', 'Redwood Estates',
           'Rail Road Flat', 'Riverbank', 'Redwood Valley', 'Rio Nido', 'Redway', 'Rio Dell', 'Redcrest',
           'Rancho Cordova', 'Represa', 'Rio Linda', 'Rio Oso', 'River Pines', 'Rocklin', 'Ryde', 'Rackerby',
           'Richvale', 'Rough And Ready', 'Red Bluff', 'Ravendale', 'Rota', 'Rainier', 'Rhododendron', 'Rufus',
           'Rickreall', 'Reedsport', 'Riddle', 'Roseburg', 'Rogue River', 'Ravensdale', 'Renton', 'Rollingbay', 'REI',
           'Randle',
           'Retsil', 'Ryderwood', 'Rosburg', 'Ronald', 'Reardan', 'Ritzville', 'Royal City', 'Red Devil',
           'Russian Mission', 'Rampart']
SCities = ['Sabana Grande', 'San German', 'San Sebastian', 'Sabana Hoyos', 'San Antonio', 'Salinas',
           'San Lorenzo', 'Santa Isabel', 'St Thomas', 'St John', 'San Juan', 'Sabana Seca', 'Saint Just', 'Shutesbury',
           'Southampton', 'South Barre', 'South Hadley', 'Southwick', 'Springfield', 'Sandisfield', 'Savoy',
           'Sheffield', 'South Egremont',
           'Southfield', 'South Lee', 'Stockbridge', 'Shelburne Falls', 'South Deerfield', 'Sunderland', 'Shirley',
           'Still River', 'Shrewsbury', 'Southbridge', 'South Grafton', 'South Lancaster', 'Spencer', 'Sterling',
           'Sturbridge', 'Sutton', 'Sherborn', 'Southborough', 'Stow', 'Sudbury', 'Saugus', 'Swampscott', 'Salisbury',
           'Salem', 'South Hamilton', 'Scituate', 'Sharon', 'Sheldonville', 'South Walpole', 'Stoughton',
           'South Boston', 'Somerville', 'Stoneham', 'South Weymouth', 'South Carver', 'South Easton', 'Sagamore',
           'Sagamore Beach', 'Sandwich', 'Siasconset', 'Silver Beach', 'South Chatham', 'South Dennis', 'South Harwich',
           'South Orleans', 'South Wellfleet', 'South Yarmouth', 'Somerset', 'South Dartmouth', 'Seekonk', 'Swansea',
           'Saunderstown', 'Shannock', 'Slatersville', 'Slocum', 'Smithfield', 'Sanbornton', 'South Newbury',
           'South Sutton', 'Stinson Lake', 'Suncook', 'Sullivan', 'Swanzey', 'Spofford', 'Stoddard', 'Sugar Hill',
           'South Acworth', 'Sunapee', 'South Hampton', 'Sanbornville', 'Sandown', 'Seabrook', 'Silver Lake',
           'Somersworth', 'South Tamworth', 'Strafford', 'Stratham', 'South Berwick', 'Sebago', 'Scarborough', 'Saco',
           'Sanford', 'Shapleigh', 'South Casco', 'South Freeport', 'South Windham', 'Springvale', 'Standish',
           'Steep Falls', 'South Portland', 'Sabattus', 'South Paris', 'Sumner', 'South China', 'South Gardiner',
           'Sangerville', 'Sebec', 'Shirley Mills', 'Stetson', 'Stillwater', 'Sebasco Estates', 'South Bristol',
           'Squirrel Island', 'Southport', 'Salsbury Cove', 'Sargentville', 'Seal Cove', 'Seal Harbor', 'Sedgwick',
           'Sorrento', 'Southwest Harbor', 'Steuben', 'Stonington', 'Sunset', 'Surry', 'Swans Island', 'Saint Agatha',
           'Saint David', 'Saint Francis', 'Sheridan', 'Sherman', 'Stacyville', 'Sinclair', 'Smyrna Mills', 'Stockholm',
           'South Thomaston', 'Spruce Head', 'Saint Albans', 'Sandy Point', 'Searsmont', 'Searsport', 'Shawmut',
           'Skowhegan', 'Solon', 'Stockton Springs', 'Stratton', 'Strong', 'South Pomfret', 'South Royalton',
           'South Ryegate', 'South Strafford', 'South Woodstock', 'Saxtons River', 'South Londonderry', 'Shaftsbury',
           'South Newfane', 'Stamford', 'South Burlington', 'S BTV', 'SMC', 'Saint Albans Bay', 'Shelburne', 'Sheldon',
           'Sheldon Springs', 'South Hero', 'Starksboro', 'Swanton', 'Stowe', 'Shoreham', 'Saint Johnsbury',
           'Saint Johnsbury Center', 'Simsbury', 'Somers', 'Somersville', 'South Glastonbury', 'South Windsor',
           'Stafford', 'Stafford Springs', 'Staffordville', 'Suffield', 'Scotland', 'South Willington',
           'Storrs Mansfield', 'South Lyme', 'Sandy Hook', 'Seymour', 'Shelton', 'South Britain', 'Southbury',
           'Southington', 'Stevenson', 'Stratford', 'South Kent', 'Scotch Plains', 'Sewaren', 'Short Hills',
           'South Orange', 'South Plainfield', 'Secaucus', 'Saddle River', 'Sussex', 'South Hackensack', 'Saddle Brook',
           'Spring Lake', 'Schooleys Mountain', 'Sparta', 'Stanhope', 'Succasunna', 'Swartswood', 'Summit', 'Stirling',
           'South Harrison Township', 'Sewell', 'Sicklerville', 'Somerdale', 'Swedesboro', 'Shamong', 'Sea Isle City',
           'Somers Point', 'South Seaville', 'Stone Harbor', 'Strathmere', 'Shiloh', 'Sergeantsville', 'Skillman',
           'Stockton', 'Sea Girt', 'Seaside Heights', 'Seaside Park', 'Sayreville', 'South Amboy', 'South Bound Brook',
           'South River', 'Spotswood', 'Stanton', 'Stewartsville', 'Staten Island', 'Scarsdale', 'Shenorock',
           'Shrub Oak', 'South Salem', 'Suffern', 'Slate Hill', 'Sloatsburg', 'Southfields', 'Sparkill',
           'Spring Valley', 'Sterling Forest', 'Stony Point', 'Sugar Loaf', 'South Floral Park', 'Sunnyside',
           'Springfield Gardens', 'South Richmond Hill', 'South Ozone Park', 'Sea Cliff', 'Syosset', 'Saint James',
           'Sayville', 'Seaford', 'Selden', 'Smithtown', 'Sound Beach', 'Stony Brook', 'Sagaponack', 'Sag Harbor',
           'Shelter Island', 'Shelter Island Heights', 'South Jamesport', 'Southold', 'Speonk', 'Sand Lake',
           'Schaghticoke', 'Schenevus', 'Schodack Landing', 'Schoharie', 'Selkirk', 'Slingerlands', 'Sloansville',
           'South Bethlehem', 'Speculator', 'Spencertown', 'Sprakers', 'Stephentown', 'Stottville', 'Stuyvesant',
           'Stuyvesant Falls', 'Surprise', 'Schenectady', 'Saugerties', 'Shandaken', 'Shokan', 'South Cairo',
           'Spring Glen', 'Stone Ridge', 'Salisbury Mills', 'Salt Point', 'Staatsburg', 'Stanfordville', 'Stormville',
           'Smallwood', 'South Fallsburg', 'Sparrow Bush', 'Summitville', 'Swan Lake', 'South Glens Falls', 'Sabael',
           'Saratoga Springs', 'Schroon Lake', 'Schuylerville', 'Severance', 'Shushan', 'Silver Bay', 'Stony Creek',
           'Saint Regis Falls', 'Saranac', 'Saranac Lake', 'Schuyler Falls', 'Sandy Creek', 'Savannah', 'Scipio Center',
           'Seneca Falls', 'Skaneateles', 'Skaneateles Falls', 'South Butler', 'South Otselic', 'Sylvan Beach',
           'Syracuse', 'Saint Johnsville', 'Salisbury Center', 'Sangerfield', 'Sauquoit', 'Schuyler Lake',
           'Sharon Springs', 'Sherburne', 'Sherrill', 'Smyrna', 'Solsville', 'Springfield Center', 'Stittville',
           'Sackets Harbor', 'South Colton', 'Star Lake', 'Sidney', 'Sidney Center', 'Smithboro', 'Smithville Flats',
           'South Kortright', 'South New Berlin', 'South Plymouth', 'Sanborn', 'Sandusky', 'Sardinia', 'Silver Creek',
           'South Dayton', 'South Wales', 'Spring Brook', 'Springville', 'Stella Niagara', 'Strykersville',
           'Scottsburg', 'Scottsville', 'Seneca Castle', 'Shortsville', 'Silver Springs', 'Sodus', 'Sodus Point',
           'Sonyea', 'South Byron', 'South Lima', 'Spencerport', 'Springwater', 'Stanley', 'Saint Bonaventure',
           'Salamanca', 'Sinclairville', 'Steamburg', 'Savona', 'Scio', 'Slaterville Springs', 'Swain', 'Shippingport',
           'Slovan', 'South Heights', 'Sturgeon', 'Sutersville', 'South Park', 'Sewickley', 'Springdale',
           'Scenery Hill', 'Southview', 'Spraggs', 'Strabane', 'Sycamore', 'Smithton', 'Smock', 'Star Junction',
           'Stockdale', 'Schellsburg', 'Shanksville', 'Sipesville', 'Springs', 'Stoystown', 'Salina', 'Saltsburg',
           'Schenley', 'Scottdale', 'Slickville', 'Southwest', 'Spring Church', 'Stahlstown', 'Saint Benedict',
           'Shelocta', 'Spangler', 'Sprankle Mills', 'Starford', 'Saint Marys', 'Sigel', 'Sinnamahoning', 'Stump Creek',
           'Summerville', 'Sykesville', 'Saint Michael', 'Salix', 'Seanor', 'Seward', 'Sidman', 'South Fork',
           'Strongstown', 'Summerhill', 'Saint Petersburg', 'Sarver', 'Saxonburg', 'Slippery Rock', 'Sandy Lake',
           'Sharpsville', 'Sheakleyville', 'Stoneboro', 'Seminole', 'Shippenville', 'Sligo', 'Smicksburg',
           'Snydersburg', 'Strattanville', 'Seneca', 'Sugar Grove', 'Saegertown', 'Spartansburg', 'Springboro',
           'Spring Creek', 'St Clairsville', 'Saint Boniface', 'Sandy Ridge', 'Saxton', 'Six Mile Run', 'Smithmill',
           'Smokerun', 'Sproul', 'Spruce Creek', 'Shinglehouse', 'Smethport', 'State College', 'Shawville', 'Snow Shoe',
           'Spring Mills', 'Sabinsville', 'Sylvania', 'Schaefferstown', 'Shermans Dale', 'Summerdale', 'Saint Thomas',
           'Saltillo', 'Shade Gap', 'Shady Grove', 'Shippensburg', 'Shirleysburg', 'South Mountain', 'Spring Run',
           'State Line', 'Seven Valleys', 'Spring Grove', 'Stewartstown', 'Silver Spring', 'Smoketown', 'Stevens',
           'Strasburg', 'Salona', 'Shunk', 'Slate Run', 'Sunbury', 'Selinsgrove', 'Shamokin', 'Shamokin Dam',
           'Snydertown', 'Swengel', 'Sacramento', 'Saint Clair', 'Schuylkill Haven', 'Seltzer', 'Shenandoah',
           'Summit Station', 'Schnecksville', 'Slatedale', 'Slatington', 'Springtown', 'Stockertown', 'Sumneytown',
           'Saint Johns', 'Sheppton', 'Sugarloaf', 'Summit Hill', 'Sybertsville', 'Saylorsburg', 'Sciota', 'Scotrun',
           'Shawnee On Delaware', 'Skytop', 'Stroudsburg', 'Swiftwater', 'Shohola', 'South Canaan', 'South Sterling',
           'Starlight', 'Starrucca', 'Scranton', 'Shawanese', 'Shickshinny', 'Sweet Valley', 'Shavertown', 'Sayre',
           'South Gibson', 'South Montrose', 'Stevensville', 'Sugar Run', 'Susquehanna', 'Salford', 'Salfordville',
           'Sellersville', 'Silverdale', 'Solebury', 'Souderton', 'Spinnerstown', 'Sharon Hill', 'Swarthmore',
           'Sadsburyville', 'Suplee', 'Southeastern', 'Saint Peters', 'Sassamansville', 'Schwenksville', 'Skippack',
           'Spring City', 'Spring House', 'Spring Mount', 'Shartlesville', 'Shoemakersville', 'Strausstown',
           'Saint Georges', 'Selbyville', 'Saint Inigoes', 'Saint Leonard', 'Saint Marys City', 'Solomons',
           'Southern Md Facility', 'Suitland', 'Savage', 'Shady Side', 'Sandy Spring', 'Spencerville',
           'Suburb Maryland Fac', 'Severn', 'Severna Park', 'Simpsonville', 'Sparks Glencoe', 'Street',
           'Sparrows Point', 'Spring Gap', 'Saint Michaels', 'Secretary', 'Sherwood', 'Still Pond', 'Sudlersville',
           'Sabillasville', 'Sharpsburg', 'Smithsburg', 'Sharptown', 'Showell', 'Snow Hill', 'Sealston', 'Sharps',
           'Spotsylvania', 'Star Tannery', 'Stephens City', 'Stephenson', 'Sperryville', 'Stevensburg', 'Sumerduck',
           'Syria', 'Singers Glen', 'Schuyler', 'Shipman', 'Stanardsville', 'Saint Stephens Church', 'Saluda',
           'Sandston', 'Schley', 'Shacklefords', 'State Farm', 'Studley', 'Susan', 'Saxis', 'Seaview', 'Suffolk',
           'Sedley', 'Skippers', 'Sutherland', 'Saxe', 'Skipwith', 'South Hill', 'Sandy Level', 'Shawsville',
           'Staffordsville', 'Stanleytown', 'Stuart', 'Saint Charles', 'Saint Paul', 'Saltville', 'Speedwell',
           'Staunton', 'Selma', 'Steeles Tavern', 'Stuarts Draft', 'Swoope', 'Spout Spring', 'Sutherlin', 'Sweet Briar',
           'Shortt Gap', 'Swords Creek', 'Simon', 'Squire', 'Switchback', 'Secondcreek', 'Sinks Grove', 'Smoot',
           'Saxon', 'Seth', 'Sharples', 'Smithers', 'Southside', 'Sylvester', 'Sandyville', 'Shenandoah Junction',
           'Shepherdstown', 'Slanesville', 'Summit Point', 'Salt Rock', 'Scott Depot', 'Shoals', 'Sod', 'Spurlockville',
           'Sumerco', 'Sarah Ann', 'Stollings', 'Switzer', 'Saulsville', 'Sabine', 'Scarbro', 'Shady Spring', 'Skelton',
           'Slab Fork', 'Sophia', 'Spanishburg', 'Stanaford', 'Surveyor', 'Sandstone', 'Spring Dale', 'Short Creek',
           'Sistersville', 'Smithville', 'Snowshoe', 'Slatyfork', 'Sand Fork', 'Shinnston', 'Simpson', 'Smithburg',
           'Spelter', 'Shock', 'Summersville', 'Swiss', 'Shanks', 'Seneca Rocks', 'Siloam', 'Stoneville', 'Saxapahaw',
           'Seagrove', 'Sedalia', 'Semora', 'Siler City', 'Snow Camp', 'Southmont', 'Staley', 'Star', 'Stokesdale',
           'Summerfield', 'Swepsonville', 'SJAFB', 'Stem', 'Stovall', 'Saratoga', 'Scotland Neck', 'Seaboard', 'Sims',
           'Speed', 'Spring Hope', 'Stantonsburg', 'Stokes', 'Swanquarter', 'Salvo', 'Shawboro', 'South Mills',
           'Stumpy Point', 'Shelby', 'Spindale', 'Stanfield', 'Saint Pauls', 'Salemburg', 'Shannon', 'Southern Pines',
           'Stedman', 'Shallotte', 'Sneads Ferry', 'Supply', 'Sunset Beach', 'Salter Path', 'Sealevel', 'Seven Springs',
           'Stacy', 'Stella', 'Stonewall', 'Swansboro', 'Statesville', 'Scottville', 'Sherrills Ford', 'State Road',
           'Scotts', 'Sapphire', 'Scaly Mountain', 'Skyland', 'Spruce Pine', 'Swannanoa', 'Sylva', 'Saint Matthews',
           'Salley', 'Santee', 'Silverstreet', 'State Park', 'Summerton', 'Sumter', 'Shaw A F B', 'Spartanburg',
           'Startex', 'Saint George', 'Saint Stephen', 'Smoaks', 'Sullivans Island', 'Salters', 'Sellers',
           'Society Hill', 'Sandy Springs', 'Six Mile', 'Slater', 'Starr', 'Saint Helena Island', 'Scotia', 'Suwanee',
           'Social Circle', 'Snellville', 'Stone Mountain', 'Sargent', 'Senoia', 'Sunny Side', 'Swainsboro', 'Sardis',
           'Soperton', 'Statesboro', 'Stillmore', 'Sautee Nacoochee', 'Suches', 'Statham', 'Stephens', 'Sugar Valley',
           'Stapleton', 'Sandersville', 'Seville', 'Shady Dale', 'Smarr', 'Sapelo Island', 'Saint Simons Island',
           'Screven', 'Sea Island', 'Surrency', 'Sparks', 'Statenville', 'Sale City', 'Saint Augustine', 'Sanderson',
           'Starke', 'San Mateo', 'Satsuma', 'Sparr', 'Sumatra', 'Saint Marks', 'Sopchoppy', 'Steinhatchee',
           'Santa Rosa Beach', 'Sneads', 'Shalimar', 'Suwannee', 'Scottsmoor', 'Satellite Beach', 'Sebastian',
           'Sharpes', 'Summerland Key', 'South Bay', 'Sun City Center', 'Saint Leo', 'Seffner', 'Sumterville',
           'Sun City', 'Sydney', 'Sebring', 'Saint James City', 'Sanibel', 'Sarasota', 'Spring Hill', 'Safety Harbor',
           'Saint Cloud', 'Saginaw', 'Siluria', 'Sterrett', 'Sumiton', 'Sylacauga', 'Samantha', 'Sipsey', 'Sulligent',
           'Scottsboro', 'Section', 'Steele', 'Shorter', 'Spring Garden', 'Shorterville', 'Skipperville', 'Slocomb',
           'Samson', 'Spanish Fort', 'Saint Elmo', 'Saint Stephens', 'Saraland', 'Semmes', 'Silverhill', 'Sunflower',
           'Safford', 'Sawyerville', 'Sweet Water', 'Seale', 'Smiths Station', 'Silas', 'Shelbyville', 'Slayden',
           'Stewart', 'Sale Creek', 'Sequatchie', 'Sewanee', 'Signal Mountain', 'Smartt', 'Soddy Daisy',
           'South Pittsburg', 'Shady Valley', 'Sevierville', 'Sharps Chapel', 'Shawanee', 'Sneedville',
           'Strawberry Plains', 'Sunbright', 'Surgoinsville', 'Sweetwater', 'Saulsbury', 'Samburg', 'South Fulton',
           'Scotts Hill', 'Selmer', 'Silerton', 'Stantonville', 'Sugar Tree', 'Saint Joseph', 'Santa Fe', 'Summertown',
           'Silver Point', 'Sarah', 'Senatobia', 'Sherard', 'Sledge', 'Southaven', 'Scott', 'Shaw', 'Schlater',
           'Scobey', 'Sidon', 'Slate Spring', 'Swiftown', 'Sallis', 'Sandhill', 'Satartia', 'Sibley', 'Silver City',
           'Scooba', 'Sebastopol', 'Shubuta', 'Shuqualak', 'Seminary', 'Soso', 'Stringer', 'Sumrall',
           'Stennis Space Center', 'Saucier', 'Smithdale', 'Sontag', 'Starkville', 'Steens', 'Sturgis', 'Sasser',
           'Shellman', 'Saint Catharine', 'Saint Mary', 'Sulphur', 'Shepherdsville', 'Stephensport', 'Sadieville',
           'Salt Lick', 'Salvisa', 'Slade', 'Stamping Ground', 'Sandgap', 'Stanford', 'Siler', 'Stinnett', 'Saul',
           'Scalf', 'Sextons Creek', 'Stoney Fork', 'Sanders', 'Silver Grove', 'Soldier', 'South Portsmouth',
           'South Shore', 'Sitka', 'Stambaugh', 'Saint Helens', 'Salyersville', 'South Williamson', 'Shelbiana',
           'Shelby Gap', 'Stone', 'Stopover', 'Stanville', 'Sassafras', 'Scuddy', 'Sizerock', 'Slemp', 'Smilax', 'Seco',
           'Smithland', 'Symsonia', 'Summer Shade', 'Smiths Grove', 'Sharon Grove', 'Sweeden', 'South Carrollton',
           'Sebree', 'Slaughters', 'Smith Mills', 'Spottsville', 'Science Hill', 'Stearns', 'Strunk', 'Sonora',
           'Saint Louisville', 'Saint Paris', 'South Bloomingville', 'South Solon', 'Stoutsville', 'Shauck',
           'Stony Ridge', 'Stryker', 'Salesville', 'Sarahsville', 'Senecaville', 'Shawnee', 'Stockport', 'Stone Creek',
           'Salineville', 'Shadyside', 'Saint Clairsville', 'Steubenville', 'Sheffield Lake', 'Strongsville',
           'Streetsboro', 'Sharon Center', 'Struthers', 'Sherrodsville', 'Shreve', 'Sugarcreek', 'Sulphur Springs',
           'Seven Mile', 'Shandon', 'South Lebanon', 'Sabina', 'Sinking Spring', 'South Charleston', 'South Vienna',
           'Scioto Furnace', 'Scottown', 'Seaman', 'South Point', 'South Webster', 'Stout', 'Shade', 'Saint Henry',
           'Stilesville', 'Speedway', 'Saint John', 'San Pierre', 'Schererville', 'Schneider', 'Sumava Resorts',
           'Shipshewana', 'South Bend', 'Saint Joe', 'South Milford', 'South Whitley', 'Stroh', 'Servia', 'Star City',
           'Swayzee', 'Sweetser', 'Sunman', 'Sellersburg', 'Scipio', 'Salamonia', 'Spiceland', 'Springport', 'Straughn',
           'Solsberry', 'Stinesville', 'Switz City', 'Saint Anthony', 'Saint Croix', 'Saint Meinrad', 'Sandborn',
           'Santa Claus', 'Schnellville', 'Spurgeon', 'Stendal', 'Saint Bernice', 'Saint Mary Of The Woods',
           'Seelyville', 'Shelburn', 'Shepardsville', 'Stockwell', 'Smiths Creek', 'Saint Clair Shores', 'Saline',
           'Samaria', 'South Lyon', 'South Rockwood', 'Southgate', 'Sterling Heights', 'Snover', 'Swartz Creek',
           'Saint Helen', 'Sebewaing', 'Silverwood', 'South Branch', 'Spruce', 'Saint Louis', 'Shaftsburg', 'Shepherd',
           'Six Lakes', 'Sunfield', 'Schoolcraft', 'South Haven', 'Sawyer', 'Sand Creek', 'Somerset Center',
           'Spring Arbor', 'Stanwood', 'Saugatuck', 'Sears', 'South Boardman', 'Suttons Bay', 'Saint Ignace',
           'Sault Sainte Marie', 'Sagola', 'Seney', 'Shingleton', 'Skandia', 'Spalding', 'Sidnaw', 'Skanee',
           'South Range', 'Searsboro', 'Sheldahl', 'State Center', 'Story City', 'Sully', 'Swan', 'Saint Ansgar',
           'Scarville', 'Swaledale', 'Sac City', 'Sioux Rapids', 'Storm Lake', 'Swea City', 'Shell Rock',
           'Steamboat Rock', 'Shannon City', 'Schaller', 'Sergeant Bluff', 'Sloan', 'Sioux City', 'Sioux Center',
           'Spirit Lake', 'Superior', 'Schleswig', 'Shambaugh', 'Sabula', 'Saint Donatus', 'Saint Olaf', 'Spragueville',
           'Springbrook', 'Strawberry Point', 'Saint Lucas', 'Spillville', 'Shellsburg', 'South Amana', 'South English',
           'Swisher', 'Sigourney', 'Sperry', 'Swedesburg', 'Saukville', 'Sheboygan', 'Sheboygan Falls', 'Slinger',
           'South Milwaukee', 'Sturtevant', 'Sauk City', 'Sextonville', 'Shullsburg', 'South Wayne', 'Spring Green',
           'Sun Prairie', 'Sinsinawa', 'Stitzer', 'Saint Croix Falls', 'Star Prairie', 'Shawano', 'Shiocton',
           'Sobieski', 'Suamico', 'Suring', 'Saint Nazianz', 'Sister Bay', 'Sturgeon Bay', 'Schofield', 'Stetsonville',
           'Stevens Point', 'Summit Lake', 'Saint Germain', 'Sayner', 'Soldiers Grove', 'Strum', 'Spooner', 'Sarona',
           'Shell Lake', 'Siren', 'Solon Springs', 'Stone Lake', 'Saxeville', 'Scandinavia', 'Saint Paul Park',
           'Scandia', 'Shafer', 'South Saint Paul', 'Stanchfield', 'Saint Bonifacius', 'Santiago', 'Shakopee',
           'Spring Park', 'Saint Louis Park', 'Schroeder', 'Side Lake', 'Soudan', 'Sturgeon Lake', 'Swan River',
           'Swatara', 'Sargeant', 'Stewartville', 'Saint Peter', 'Searles', 'Sleepy Eye', 'Sherburn', 'Slayton',
           'Steen', 'Storden', 'Sacred Heart', 'Seaforth', 'Spicer', 'Sunburg', 'Saint Martin', 'Sartell',
           'Sauk Centre', 'Sauk Rapids', 'Starbuck', 'Swanville', 'Sebeka', 'Staples', 'Sabin', 'Shelly', 'Shevlin',
           'Solway', 'South International Falls', 'Squaw Lake', 'Swift', 'Saint Hilaire', 'Saint Vincent', 'Salol',
           'Stephen', 'Strandquist', 'Strathcona', 'Sinai', 'Sioux Falls', 'Sisseton', 'Strandburg', 'Stephan',
           'Saint Lawrence', 'Stickney', 'Selby', 'Saint Onge', 'Scenic', 'Smithwick', 'Spearfish', 'Stirum', 'Sarles',
           'Sheyenne', 'Starkweather', 'Spiritwood', 'Streeter', 'Sykeston', 'Selfridge', 'Shields', 'Solen',
           'Sentinel Butte', 'South Heart', 'Souris', 'Surrey', 'Saint Xavier', 'Sand Springs', 'Silver Gate',
           'Saint Marie', 'Sand Coulee', 'Simms', 'Stockett', 'Sunburst', 'Sun River', 'Sweet Grass', 'Silver Star',
           'Saint Ignatius', 'Saint Regis', 'Saltese', 'Seeley Lake', 'Sula', 'Skokie', 'Streamwood', 'Schaumburg',
           'Stone Park', 'Schiller Park', 'South Elgin', 'Shorewood', 'South Holland', 'South Wilmington', 'Steger',
           'Summit Argo', 'Serena', 'Shabbona', 'Somonauk', 'Steward', 'Saint Anne', 'Stockland', 'Savanna',
           'Scales Mound', 'Shirland', 'South Beloit', 'Stillman Valley', 'Sherrard', 'Silvis', 'Seatonville',
           'Standard', 'Streator', 'Sublette', 'Seaton', 'Smithshire', 'Speer', 'Stronghurst', 'South Pekin',
           'Sparland', 'Saunemin', 'Saybrook', 'Secor', 'Strawn', 'Sadorus', 'Sidell', 'Sorento', 'South Roxana',
           'Scott Air Force Base', 'Saint Jacob', 'Saint Libory', 'Steeleville', 'Sutter', 'Sainte Marie',
           'Saint Francisville', 'Shumway', 'Stewardson', 'Stoy', 'San Jose', 'Sailor Springs', 'Sandoval', 'Scheller',
           'Sesser', 'Shobonier', 'Springerton', 'Shawneetown', 'Stonefort', 'Saint Ann', 'Silex', 'Saint Patrick',
           'Saverton', 'Shelbina', 'Sainte Genevieve', 'Scott City', 'Sedgewickville', 'Sturdivant', 'Sikeston',
           'Senath', 'Shook', 'Silva', 'Skidmore', 'Stanberry', 'Spickard', 'Stet', 'Schell City', 'Sarcoxie',
           'South West City', 'Stark City', 'Saint Elizabeth', 'Steedman', 'Stover', 'Sunrise Beach', 'Sweet Springs',
           'Solo', 'Steelville', 'Stoutland', 'Success', 'Saint Robert', 'Seligman', 'Shell Knob', 'South Greenfield',
           'Spokane', 'Squires', 'Stotts City', 'SMSU', 'Stilwell', 'SM', 'Shawnee Mission', 'Sabetha', 'Savonburg',
           'Scammon', 'Stark', 'Strong City', 'Smith Center', 'Severy', 'Spivey', 'Sedan', 'Solomon', 'Sylvan Grove',
           'South Hutchinson', 'Sylvia', 'Schoenchen', 'Satanta', 'Spearville', 'St Columbans', 'Scribner', 'Shickley',
           'Shubert', 'Sprague', 'Staplehurst', 'Steele City', 'Steinauer', 'Strang', 'Saint Edward', 'Snyder',
           'Stromsburg', 'Saint Helena', 'South Sioux City', 'Springview', 'Saronville', 'Stockville', 'Scottsbluff',
           'Saint Bernard', 'Saint Rose', 'Schriever', 'SLU', 'Slidell', 'Sun', 'Saint Martinville', 'Singer', 'Starks',
           'Sugartown', 'Saint Amant', 'Saint Gabriel', 'Slaughter', 'Sunshine', 'Sarepta', 'Shongaloo', 'Springhill',
           'Shreveport', 'Simsboro', 'Sondheimer', 'Spearsville', 'Start', 'Sterlington', 'Swartz', 'Saint Landry',
           'Sicily Island', 'Simmesport', 'Saint Maurice', 'Sieper', 'Sikes', 'Slagle', 'Smackover', 'Sparkman',
           'Stamps', 'Story', 'Searcy', 'Solgohachia', 'Stuttgart', 'Sweet Home', 'Snow Lake', 'State University',
           'Strawberry', 'Swifton', 'Saffell', 'Sage', 'Salado', 'Sturkie', 'Sulphur Rock', 'Siloam Springs', 'Summers',
           'Subiaco', 'Springer', 'Seiling', 'Sentinel', 'Southard', 'Shattuck', 'SS', 'Sapulpa', 'Shamrock',
           'Skiatook', 'Slick', 'S Coffeyville', 'STW', 'Stroud', 'Spavinaw', 'Schulter', 'Stidham', 'Stigler', 'Snow',
           'Stringtown', 'Shidler', 'Soper', 'Swink', 'Sasakwa', 'Sallisaw', 'Shady Point', 'Spiro', 'Sachse', 'Scurry',
           'Seagoville', 'Sunnyvale', 'SBC ATT', 'Scroggins', 'Sulphur Bluff', 'Selman City', 'Sacul', 'Streetman',
           'SFA', 'S F A U', 'S F A', 'San Augustine', 'Southlake', 'Sadler', 'Saint Jo', 'Sanger', 'Southmayd',
           'Sheppard AFB', 'Stephenville', 'Santo', 'Schwertner', 'Satin', 'San Saba', 'Santa Anna', 'San Angelo',
           'Silver', 'Sterling City', 'Splendora', 'Spring', 'San Felipe', 'Sealy', 'Simonton', 'Sugar Land', 'Sweeny',
           'South Houston', 'Sabine Pass', 'Silsbee', 'Sour Lake', 'Spurger', 'Stowell', 'Shiro', 'Snook', 'Seadrift',
           'Shiner', 'Sublime', 'San Ygnacio', 'Spring Branch', 'Saint Hedwig', 'Schertz', 'Seguin', 'Smiley',
           'Sutherland Springs', 'Sandia', 'San Diego', 'Sarita', 'Sinton', 'Salineno', 'San Benito', 'San Isidro',
           'San Perlita', 'Santa Elena', 'Santa Maria', 'Santa Rosa', 'Sullivan City', 'South Padre Island',
           'San Marcos', 'Spicewood', 'Sabinal', 'Schulenburg', 'Sam Norwood', 'Skellytown', 'Spearman', 'Springlake',
           'Sunray', 'Silverton', 'South Plains', 'Seagraves', 'Shallowater', 'Slaton', 'Smyer', 'Spade', 'Spur',
           'Sudan', 'Sundown', 'Saragosa', 'Salt Flat', 'San Elizario', 'Sierra Blanca', 'Silver Plume',
           'Steamboat Springs', 'Silverthorne', 'Seibert', 'Simla', 'Sheridan Lake', 'Sugar City', 'Saguache',
           'San Luis', 'Salida', 'Sargents', 'Snowmass Village', 'Silt', 'Snowmass', 'Savery', 'Shell', 'Shirley Basin',
           'Shoshoni', 'Sundance', 'Saddlestring', 'Shelley', 'Soda Springs', 'Swanlake', 'Shoshone', 'Sun Valley',
           'Swan Valley', 'Salmon', 'Shoup', 'Stites', 'Sweet', 'Sagle', 'Saint Maries', 'Sandpoint', 'Santa',
           'Smelterville', 'Sandy', 'South Jordan', 'Salt Lake City', 'SLC', 'SSL', 'Snowville', 'Santaquin', 'Sigurd',
           'Spanish Fork', 'Santa Clara', 'Sevier', 'San Tan Valley', 'Sacaton', 'Scottsdale', 'Salome', 'Somerton',
           'Sun City West', 'San Carlos', 'Sahuarita', 'San Manuel', 'San Simon', 'Sasabe', 'Sells', 'Sierra Vista',
           'Sonoita', 'Show Low', 'Snowflake', 'Springerville', 'Second Mesa', 'Shonto', 'Sedona', 'Skull Valley',
           'Supai', 'Sandia Park', 'San Fidel', 'San Rafael', 'Santo Domingo Pueblo', 'San Ysidro', 'Sheep Springs',
           'Smith Lake', 'Shiprock', 'Sanostee', 'SF', 'San Cristobal', 'Santa Cruz', 'Serafina', 'Sapello', 'Solano',
           'Socorro', 'San Acacia', 'Santa Teresa', 'San Miguel', 'Sunland Park', 'Saint Vrain', 'San Patricio',
           'Sunspot', 'San Jon', 'Searchlight', 'Silverpeak', 'Schurz', 'Smith', 'Stateline', 'South Gate',
           'Santa Monica', 'Santa Fe Springs', 'San Pedro', 'Seal Beach', 'Surfside', 'Signal Hill', 'Sierra Madre',
           'South Pasadena', 'Sunland', 'San Marino', 'San Fernando', 'Sylmar', 'Santa Clarita', 'Stevenson Ranch',
           'Sherman Oaks', 'Studio City', 'South El Monte', 'San Dimas', 'San Gabriel', 'San Luis Rey', 'Santa Ysabel',
           'Solana Beach', 'Seeley', 'Salton City', 'Skyforest', 'San Bernardino', 'San Jacinto', 'San Clemente',
           'San Juan Capistrano', 'Silverado', 'Santa Ana', 'Santa Paula', 'Simi Valley', 'Somis', 'Summerland',
           'Santa Barbara', 'Sequoia National Park', 'Shafter', 'Strathmore', 'San Luis Obispo', 'San Ardo',
           'San Simeon', 'Santa Margarita', 'Santa Ynez', 'Solvang', 'San Joaquin', 'Santa Rita Park', 'Shaver Lake',
           'South Dos Palos', 'Sultana', 'Squaw Valley', 'San Lucas', 'Seaside', 'Soledad', 'Spreckels', 'San Bruno',
           'San Gregorio', 'SSF', 'South San Francisco', 'San Francisco', 'San Leandro', 'San Ramon', 'Suisun City',
           'Sunol', 'San Pablo', 'San Anselmo', 'San Geronimo', 'San Quentin', 'Sausalito', 'Stinson Beach',
           'San Juan Bautista', 'San Martin', 'Scotts Valley', 'Soquel', 'San Andreas', 'Snelling', 'Soulsbyville',
           'Stevinson', 'Sonoma', 'Stewarts Point', 'Salyer', 'Samoa', 'Smith River', 'Somes Bar', 'Shingle Springs',
           'Sloughhouse', 'Sutter Creek', 'Smartsville', 'Stirling City', 'Stonyford', 'Storrie', 'Strawberry Valley',
           'Shasta Lake', 'Scott Bar', 'Seiad Valley', 'Shasta', 'Shingletown', 'Sierra City', 'Sierraville',
           'Susanville', 'South Lake Tahoe', 'Schofield Barracks', 'Santa Rita', 'Saipan', 'Scappoose', 'Shaniko',
           'South Beach', 'Scotts Mills', 'Seal Rock', 'Shedd', 'Siletz', 'Stayton', 'Sublimity', 'Sixes', 'Swisshome',
           'Shady Cove', 'Sprague River', 'Summer Lake', 'Sisters', 'Spray', 'Sumpter', 'Seahurst', 'Snoqualmie',
           'Snoqualmie Pass', 'Sammamish', 'Seattle', 'Sedro Woolley', 'Shaw Island', 'Silvana', 'Skykomish',
           'Snohomish', 'Startup', 'Sultan', 'Sumas', 'Seabeck', 'Sekiu', 'Sequim', 'South Colby', 'South Prairie',
           'Southworth', 'Spanaway', 'Steilacoom', 'Suquamish', 'Salkum', 'Satsop', 'Silverlake', 'Skamokawa',
           'Soap Lake', 'Stehekin', 'Selah', 'South Cle Elum', 'Spangle', 'Steptoe', 'Saint George Island',
           'Saint Paul Island', 'Sand Point', 'Scammon Bay', 'Seldovia', 'Shageluk', 'Skwentna', 'Sleetmute',
           'Soldotna', 'South Naknek', 'Stebbins', 'Salcha', 'Savoonga', 'Selawik', 'Shaktoolik', 'Shishmaref',
           'Shungnak', 'Stevens Village', 'Skagway']
TCities = ['Toa Baja', 'Toa Alta', 'Trujillo Alto', 'Thorndike', 'Three Rivers', 'Tyringham', 'Turners Falls',
           'Templeton',
           'Townsend', 'Tewksbury', 'Tyngsboro', 'Topsfield', 'Truro', 'Taunton', 'Tiverton', 'Temple', 'Tilton',
           'Thornton', 'Troy', 'Twin Mountain', 'Tamworth', 'Topsham', 'Turner', 'Trevett', 'Tenants Harbor',
           'Thomaston', 'Taftsville', 'Thetford', 'Thetford Center', 'Tunbridge', 'Townshend', 'Taconic', 'Tariffville',
           'Tolland', 'Thompson', 'Taftville', 'Trumbull', 'Terryville', 'Torrington', 'Towaco', 'Totowa', 'Teterboro',
           'Teaneck', 'Tenafly', 'Township Of Washington', 'Tennent', 'Tranquility', 'Thorofare', 'Tuckerton',
           'Tabernacle', 'Tuckahoe', 'Titusville', 'Trenton', 'Toms River', 'Three Bridges', 'Tarrytown', 'Thornwood',
           'Tallman', 'Tappan', 'Thiells', 'Thompson Ridge', 'Tomkins Cove', 'Tuxedo Park', 'Tribes Hill',
           'Tannersville', 'Tillson', 'Tivoli', 'Thompsonville', 'Ticonderoga', 'Tupper Lake', 'Truxton', 'Tully',
           'Taberg', 'Thendara', 'Turin', 'Theresa', 'Thousand Island Park', 'Three Mile Bay', 'Tioga Center',
           'Treadwell', 'Trout Creek', 'Tunnel', 'Tonawanda', 'Troupsburg', 'Trumansburg', 'Tyrone', 'Tarentum',
           'Trafford', 'Turtle Creek', 'Taylorstown', 'Tarrs', 'Timblin', 'Torrance', 'Troutville', 'Tire Hill',
           'Twin Rocks', 'Turkey City', 'Transfer', 'Tidioute', 'Tiona', 'Tionesta', 'Townville', 'Tylersburg',
           'Tipton', 'Todd', 'Turtlepoint', 'Tioga', 'Thompsontown', 'Three Springs', 'Thomasville', 'Talmage',
           'Terre Hill', 'Trout Run', 'Turbotville', 'Trevorton', 'Troxelville', 'Tower City', 'Tremont', 'Tuscarora',
           'Tatamy', 'Treichlers', 'Trexlertown', 'Tamaqua', 'Tresckow', 'Tamiment', 'Tafton', 'Tobyhanna',
           'Tyler Hill', 'Taylor', 'Tunkhannock', 'Towanda', 'Telford', 'Trumbauersville', 'Tylersport', 'Thorndale',
           'Toughkenamon', 'Topton', 'The Plains', 'Tall Timbers', 'Temple Hills', 'Tracys Landing', 'Takoma Park',
           'Towson', 'Taylors Island', 'Templeville', 'Tilghman', 'Toddville', 'Trappe', 'Taneytown', 'Thurmont',
           'Tyaskin', 'Tylerton', 'Triangle', 'Tappahannock', 'Thornburg', 'Toms Brook', 'Timberville', 'Tyro', 'Toano',
           'Topping', 'Trevilians', 'Tangier', 'Tasley', 'Temperanceville', 'Thaxton', 'Troutdale', 'Tazewell',
           'Thorpe', 'Talcott', 'Tad', 'Tornado', 'Twilight', 'Teays', 'Thurmond', 'Triadelphia', 'Tallmansville',
           'Thomas', 'Tunnelton', 'Terra Alta', 'Toast', 'Tobaccoville', 'Trinity', 'Timberlake', 'Townsville',
           'Tarboro', 'Tillery', 'Tyner', 'Troutman', 'Tar Heel', 'Turkey', 'Tabor City', 'Teachey', 'Tarawa Terrace',
           'Taylorsville', 'Terrell', 'Traphill', 'Turnersburg', 'Tryon', 'Tuckasegee', 'Tuxedo', 'Timmonsville',
           'Turbeville', 'Tatum', 'Tamassee', 'Taylors', 'Tigerville', 'Travelers Rest', 'Tillman', 'Tucker',
           'Talking Rock', 'Tallapoosa', 'Tate', 'The Rock', 'Twin City', 'Tallulah Falls', 'Talmo', 'Tiger', 'Toccoa',
           'Turnerville', 'Toccoa Falls', 'Tignall', 'Tennga', 'Trion', 'Tunnel Hill', 'Thomson', 'Tennille',
           'Toomsboro', 'Tybee Island', 'Tifton', 'Ty Ty', 'Talbotton', 'The Villages', 'Tallahassee', 'Telogia',
           'Tangerine', 'Tavares', 'Tavernier', 'Thonotosassa', 'Trilby', 'Tampa', 'Terra Ceia', 'Tallevast',
           'Tarpon Springs', 'Talladega', 'Thorsby', 'Trussville', 'Tuscaloosa', 'Townley', 'Tanner', 'Town Creek',
           'Tuscumbia', 'Toney', 'Tallassee', 'Titus', 'Tuskegee', 'Tuskegee Institute', 'Theodore', 'Tibbie', 'Tyler',
           'Toxey', 'Tennessee Ridge', 'Thompsons Station', 'Tellico Plains', 'Tracy City', 'Tullahoma', 'Turtletown',
           'Trade', 'Talbott', 'Ten Mile', 'Thorn Hill', 'Tigrett', 'Tiptonville', 'Trezevant', 'Trimble', 'Toone',
           'Taft', 'Tiplersville', 'Tula', 'Tunica', 'Tupelo', 'Tishomingo', 'Toccopola', 'Trebloc', 'Tie Plant',
           'Tillatoba', 'Tippo', 'Tutwiler', 'Tchula', 'Terry', 'Thomastown', 'Tinsley', 'Tougaloo', 'Toomsuba',
           'Tylertown', 'Turners Station', 'Totz', 'Trosper', 'Tollesboro', 'Thelma', 'Tomahawk', 'Tutor Key',
           'Teaberry', 'Tram', 'Thousandsticks', 'Topmost', 'Tiline', 'Tolu', 'Tompkinsville', 'Tateville',
           'Thornville', 'Tarlton', 'Thurston', 'Tontogany', 'Toledo', 'Trinway', 'Tiltonsville', 'Toronto',
           'Twinsburg', 'Tallmadge', 'Tuscarawas', 'Tippecanoe', 'Tiffin', 'Tiro', 'Terrace Park', 'Tipp City',
           'Tremont City', 'Thurman', 'Tuppers Plains', 'Thorntown', 'Trafalgar', 'Tefft', 'Thayer', 'Topeka',
           'Twelve Mile', 'Taswell', 'Tell City', 'Tennyson', 'Terre Haute', 'Talbot', 'Temperance', 'Tawas City',
           'Twining', 'Tekonsha', 'Three Oaks', 'Tecumseh', 'Trufant', 'Twin Lake', 'Traverse City', 'Tustin',
           'Topinabee', 'Tower', 'Trout Lake', 'Trenary', 'Toivola', 'Tracy', 'Titonka', 'Toeterville', 'Thor',
           'Truesdale', 'Traer', 'Tripoli', 'Tingley', 'Terril', 'Treynor', 'Tabor', 'Tama', 'Troy Mills',
           'Teeds Grove', 'Trevor', 'Twin Lakes', 'Tisch Mills', 'Two Rivers', 'Tigerton', 'Three Lakes', 'Tony',
           'Tomah', 'Trempealeau', 'Tunnel City', 'Thorp', 'Trego', 'Turtle Lake', 'Tilleda', 'Taylors Falls', 'Tofte',
           'Two Harbors', 'Taconite', 'Tamarack', 'Twig', 'Taopi', 'Truman', 'Trimont', 'Trosky', 'Tintah',
           'Twin Valley', 'Talmoon', 'Tenstrike', 'Trail', 'Thief River Falls', 'Tea', 'Trent', 'Tyndall',
           'Twin Brooks', 'Tripp', 'Tolstoy', 'Tulare', 'Turton', 'Tuthill', 'Timber Lake', 'Trail City', 'Tokio',
           'Tolna', 'Tappen', 'Tuttle', 'Tolley', 'Towner', 'Teigen', 'Two Dot', 'Toston', 'Three Forks',
           'Twin Bridges', 'Thompson Falls', 'Techny', 'Tinley Park', 'Thawville', 'Tampico', 'Taylor Ridge',
           'Tiskilwa', 'Toluca', 'Tonica', 'Triumph', 'Troy Grove', 'Table Grove', 'Toulon', 'Trivoli', 'Thomasboro',
           'Tolono', 'Tuscola', 'Taylor Springs', 'Tilden', 'Tennessee', 'Timewell', 'Teutopolis', 'Trilla',
           'Taylorville', 'Tovey', 'Tower Hill', 'Tallula', 'Tamaroa', 'Texico', 'Tamms', 'Thebes', 'Treloar', 'Tiff',
           'Tarkio', 'Turney', 'Tina', 'Tiff City', 'Tebbetts', 'Triplett', 'Taneyville', 'Theodosia', 'Thornfield',
           'Tunas', 'Turners', 'Tonganoxie', 'Treece', 'Tescott', 'Turon', 'Tribune', 'Tekamah', 'Table Rock', 'Tobias',
           'Thedford', 'Thibodaux', 'Theriot', 'Talisheek', 'Tangipahoa', 'Tickfaw', 'Turkey Creek', 'Tallulah',
           'Transylvania', 'Trout', 'Tullos', 'Tillar', 'Texarkana', 'Thida', 'Tichnor', 'Traskwood', 'Turrell',
           'Tyronza', 'Trumann', 'Tuckerman', 'Tumbling Shoals', 'Timbo', 'Tilly', 'Tontitown', 'T A F B',
           'Thackerville', 'Tatums', 'Tussy', 'Terral', 'Taloga', 'Texola', 'Texhoma', 'Turpin', 'Talala', 'Terlton',
           'Tulsa', 'Twin Oaks', 'Tahlequah', 'Talihina', 'Tuskahoma', 'Tonkawa', 'The Colony', 'Trinidad', 'Talco',
           'Telephone', 'Tom Bean', 'Troup', 'Teague', 'Tennessee Colony', 'Tenaha', 'Timpson', 'Tolar', 'Throckmorton',
           'Thrall', 'Tehuacana', 'Talpa', 'Telegraph', 'Thicket', 'Tomball', 'Thompsons', 'Texas City', 'Telferner',
           'Tuleta', 'Tynan', 'Tow', 'Tarpley', 'Texline', 'Tulia', 'Tell', 'Tahoka', 'Tye', 'Tarzan', 'Toyah',
           'Toyahvale', 'Terlingua', 'Tornillo', 'Tabernash', 'Toponas', 'Timnath', 'Trinchera', 'Two Buttes', 'Towaoc',
           'Telluride', 'Tie Siding', 'Ten Sleep', 'Thermopolis', 'Teton Village', 'Thayne', 'Thatcher', 'Twin Falls',
           'Terreton', 'Teton', 'Tetonia', 'Tendoy', 'Tensed', 'Tabiona', 'Tooele', 'Tridell', 'Tremonton', 'Teasdale',
           'Toquerville', 'Torrey', 'Tropic', 'Tortilla Flat', 'Tempe', 'Tacna', 'Tolleson', 'Tonopah', 'Tonto Basin',
           'Tombstone', 'Topawa', 'Tumacacori', 'Tubac', 'Tucson', 'Tonalea', 'Tuba City', 'Topock',
           'Temple Bar Marina', 'Teec Nos Pos', 'Tsaile', 'Tijeras', 'Tome', 'Torreon', 'Thoreau', 'Tohatchi',
           'Taos Ski Valley', 'Taos', 'Tererro', 'Tesuque', 'Tierra Amarilla', 'Trampas', 'Tres Piedras', 'Truchas',
           'Truth Or Consequences', 'Taiban', 'Timberon', 'Tinnie', 'Tularosa', 'Tucumcari', 'Trementina', 'The Lakes',
           'Topanga', 'Tujunga', 'Tarzana', 'Thousand Oaks', 'Toluca Lake', 'Temple City', 'Tecate', 'Thermal',
           'Thousand Palms', 'Twentynine Palms', 'Tecopa', 'Twin Peaks', 'Temecula', 'Trabuco Canyon', 'Terra Bella',
           'Tupman', 'Tehachapi', 'Trona', 'Tollhouse', 'Tranquillity', 'Traver', 'Travis AFB', 'Tomales', 'Tres Pinos',
           'Tuolumne', 'Turlock', 'Twain Harte', 'The Sea Ranch', 'Twain', 'Tehama', 'Trinity Center', 'Termo', 'Topaz',
           'Tulelake', 'Tahoma', 'Tahoe City', 'Tahoe Vista', 'Truckee', 'Tripler Army Medical Center', 'Tamuning',
           'Tinian', 'The Dalles', 'Tualatin', 'Tygh Valley', 'Tillamook', 'Timber', 'Tolovana Park', 'Tangent',
           'Tidewater', 'Tenmile', 'Tiller', 'Talent', 'Terrebonne', 'Tracyton', 'Tacoma', 'Tumwater', 'Taholah',
           'Tahuya', 'Tenino', 'Tokeland', 'Toutle', 'Tonasket', 'Twisp', 'Tieton', 'Toppenish', 'Tekoa', 'Tumtum',
           'Touchet', 'Toksook Bay', 'Takotna', 'Talkeetna', 'Tatitlek', 'Togiak', 'Tuluksak', 'Tuntutuliak', 'Tununak',
           'Tyonek',
           'Trapper Creek', 'Tanacross', 'Tanana', 'Teller', 'Tok', 'Tenakee Springs', 'Thorne Bay']
UCities = ['Utuado', 'Upton', 'Uxbridge', 'Union', 'Unity', 'UVM', 'Underhill', 'Underhill Center', 'Unionville',
           'Uncasville', 'Union City',
           'Uniondale', 'Ulster Park', 'Upper Jay', 'Union Springs', 'Utica', 'Unadilla', 'Union Hill', 'Uniontown',
           'Uledi', 'Ursina', 'United',
           'University Park', 'Ulysses', 'Upperstrasburg', 'Unityville', 'Unity House', 'Union Dale', 'Ulster',
           'Upper Black Eddy', 'Upper Darby', 'Uwchland', 'Upperville', 'Upper Marlboro', 'Upperco', 'Upper Falls',
           'Union Bridge', 'Upper Fairmount', 'Urbanna', 'Union Hall', 'Uneeda', 'Upperglade', 'Upper Tract',
           'Union Mills', 'Union Grove', 'USC', 'UNA', 'Ulmer', 'Uvalda', 'Union Point', 'Upatoi', 'Umatilla', 'UCF',
           'Uriah', 'Unicoi', 'University', 'Union Church', 'Union Star', 'Unionville Center', 'Urbana',
           'Union Furnace', 'Upper Sandusky', 'Uhrichsville', 'Uniopolis', 'Upland', 'Underwood', 'Universal',
           'Union Lake', 'Ubly', 'University Center', 'Union Pier', 'Urbandale', 'USPS BMC', 'Ute', 'Udell',
           'Union Center', 'Upson', 'Upsala', 'Ulen', 'Upham', 'Ulm', 'Ursa', 'Ullin', 'Urich', 'Ulman', 'Udall',
           'Uehling', 'Uncle Sam', 'Urania', 'Umpire', 'UCA', 'Universal City', 'UT', 'Uvalde', 'Utopia', 'Umbarger',
           'Usaf Academy', 'Ucon', 'UNM', 'Ute Park', 'Ukiah', 'Upper Lake', 'Umpqua', 'University Place', 'Usk',
           'Unalakleet', 'Unalaska']
VCities = ['Vega Alta', 'Vega Baja', 'Vieques', 'Villalba', 'Village Of Nagog Woods', 'Vineyard Haven', 'Vienna',
           'Vanceboro', 'Van Buren',
           'Vinalhaven', 'Vassalboro', 'Vershire', 'Vernon', 'Vergennes', 'Vernon Rockville', 'Versailles', 'Voluntown',
           'Verona', 'Vauxhall',
           'Voorhees', 'Vincentown', 'Villas', 'Vineland', 'Ventnor City', 'Valhalla', 'Verplanck', 'Valley Cottage',
           'Valley Stream', 'Valatie', 'Valley Falls', 'Voorheesville', 'Vails Gate', 'Verbank', 'Victory Mills',
           'Vermontville', 'Verona Beach', 'Van Hornesville', 'Vernon Center', 'Vestal', 'Van Buren Point', 'Varysburg',
           'Victor', 'Van Etten', 'Van Voorhis', 'Venetia', 'Vestaburg', 'Vanderbilt', 'Vandergrift', 'Valier',
           'Vintondale', 'Valencia', 'Villa Maria', 'Volant', 'Vowinckel', 'Venus', 'Venango', 'Vicksburg',
           'Valley View', 'Villanova', 'Valley Forge', 'Virginville', 'Viola', 'Valley Lee', 'Village', 'Viewtown',
           'Virginia Beach', 'VAB', 'Virginia State University', 'Valentines', 'Victoria', 'Vesta', 'Villamont',
           'Vinton', 'Vesuvius', 'Vernon Hill', 'Virgilina', 'Vansant', 'Van', 'Verdunville', 'Verner', 'Varney',
           'Valley Grove', 'Volga', 'Valley Bend', 'Valley Head', 'Vaughan', 'Vale', 'Vass', 'Vandemere', 'Valdese',
           'Valle Crucis', 'Vilas', 'Vance', 'Van Wyck', 'Vaucluse', 'Varnville', 'Villa Rica', 'Vidalia', 'Varnell',
           'Valdosta', 'Valparaiso', 'Vero Beach', 'Valrico', 'Venice', 'Vandiver', 'Vincent', 'Vinemont', 'Vina',
           'Valhermoso Springs', 'Verbena', 'Vredenburgh', 'Vinegar Bend', 'Valley', 'Vanleer', 'Vonore', 'Van Vleet',
           'Vardaman', 'Vaiden', 'Valley Park', 'Vossburg', 'Vancleave', 'Vine Grove', 'Vanceburg', 'Van Lear',
           'Vancleve', 'Virgie', 'Vest', 'Vicco', 'Viper', 'Vickery', 'Vermilion', 'Valley City', 'Vandalia', 'Vanlue',
           'Van Wert', 'Vaughnsville', 'Venedocia', 'Vevay', 'Vallonia', 'Velpen', 'Vincennes', 'Veedersburg', 'Vassar',
           'Vulcan', 'Van Meter', 'Ventura', 'Varina', 'Villisca', 'Vail', 'Van Horne', 'Vining', 'Valders', 'Vesper',
           'Viroqua', 'Van Dyne', 'Vermillion', 'Virginia', 'Villard', 'Verndale', 'Vergas', 'Viking', 'Valley Springs',
           'Viborg', 'Volin', 'Veblen', 'Virgil', 'Vivian', 'Velva', 'Voltaire', 'Vida', 'Volborg', 'Vaughn',
           'Virginia City', 'Vernon Hills', 'Villa Park', 'Van Orin', 'Varna', 'Vermont', 'Villa Grove', 'Valmeyer',
           'Virden', 'Villa Ridge', 'Valles Mines', 'Vanduser', 'Viburnum', 'Vichy', 'Vanzant', 'Valley Center',
           'Verdon', 'Verdigre', 'Valentine', 'Vacherie', 'Violet', 'Varnado', 'Ville Platte', 'Ventress',
           'Vandervoort', 'Vilonia', 'Vanndale', 'Violet Hill', 'Vendor', 'Verden', 'Velma', 'Vinson', 'Vici', 'Vera',
           'Vinita', 'Valliant', 'Vian', 'Van Alstyne', 'Valley Mills', 'Valera', 'Valley Spring', 'Veribest', 'Voca',
           'Voss', 'Vancourt', 'Votaw', 'Van Vleck', 'Vidor', 'Village Mills', 'Von Ormy', 'Vanderpool', 'Vega',
           'Van Horn', 'Vona', 'Van Tassell', 'Veteran', 'Vernal', 'Virgin', 'Veyo', 'Valley Farms', 'Veguita',
           'Vanderwagen', 'Vadito', 'Valdez', 'Vallecitos', 'Velarde', 'Villanueva', 'Valmora', 'Vado', 'Valmy',
           'Verdi', 'Verdugo City', 'Van Nuys', 'Valley Village', 'Vista', 'Vidal', 'Victorville', 'Visalia',
           'Valyermo', 'Vallejo', 'Valley Ford', 'Vallecito', 'Vernalis', 'Villa Grande', 'Vineburg',
           'Vacaville', 'Volcano', 'Vernonia', 'Veneta', 'Vashon', 'Vader', 'Vancouver', 'Vantage', 'Valleyford',
           'Veradale', 'Venetie']
WCities = ['Wales', 'Ware', 'Warren', 'West Chesterfield', 'Westfield', 'West Hatfield', 'West Springfield',
           'West Warren', 'Whately',
           'Wheelwright', 'Wilbraham', 'Williamsburg', 'Woronoco', 'Worthington', 'West Stockbridge', 'Williamstown',
           'Windsor', 'Warwick',
           'Wendell', 'Wendell Depot', 'Westminster', 'West Groton', 'West Townsend', 'Winchendon',
           'Winchendon Springs', 'Webster', 'Westborough',
           'West Boylston', 'West Brookfield', 'West Millbury', 'Whitinsville', 'Worcester', 'Wayland', 'Woodville',
           'Woburn', 'Wakefield', 'West Boxford',
           'Westford', 'Wilmington', 'Winchester', 'Wenham', 'West Newbury', 'Walpole', 'Westwood', 'Wrentham',
           'West Roxbury', 'Winthrop', 'West Medford', 'Weymouth', 'West Bridgewater', 'White Horse Beach', 'Whitman',
           'Waltham', 'West Newton', 'Waban', 'Watertown', 'Waverley', 'Wellesley Hills', 'Wellesley', 'Weston',
           'Woods Hole', 'Wareham', 'West Chop', 'West Falmouth', 'West Tisbury', 'West Wareham', 'Wellfleet',
           'West Barnstable', 'West Chatham', 'West Dennis', 'West Harwich', 'West Hyannisport', 'West Yarmouth',
           'Westport', 'Westport Point', 'West Greenwich', 'Westerly', 'West Kingston', 'West Warwick',
           'Wood River Junction', 'Woonsocket', 'Wyoming', 'Wilton', 'Windham', 'Waterville Valley', 'Warner',
           'Washington', 'Weare', 'Wentworth', 'Wilmot', 'Winnisquam', 'West Nottingham', 'Woodstock', 'Westmoreland',
           'West Peterborough', 'West Swanzey', 'West Stewartstown', 'Whitefield', 'West Lebanon', 'Woodsville',
           'West Ossipee', 'Wolfeboro', 'Wolfeboro Falls', 'Wonalancet', 'Waterboro', 'Waterford', 'Wells',
           'West Baldwin', 'Westbrook', 'West Kennebunk', 'West Newfield', 'Wayne', 'Weld', 'West Bethel', 'West Minot',
           'West Paris', 'West Poland', 'Waite', 'West Enfield', 'Winn', 'Winterport', 'Wytopitlock', 'Waldoboro',
           'West Boothbay Harbor', 'Wiscasset', 'Woolwich', 'Wesley', 'Whiting', 'Winter Harbor', 'Wallagrass',
           'Washburn', 'West Rockport', 'Waterville', 'West Forks', 'West Farmington', 'White River Junction',
           'Wells River', 'West Fairlee', 'West Hartford', 'West Topsham', 'Wilder', 'Westminster Station', 'Wardsboro',
           'West Dover', 'West Dummerston', 'West Halifax', 'West Townshend', 'West Wardsboro', 'Whitingham',
           'Williamsville', 'Winooski', 'Williston', 'Waterbury', 'Waitsfield', 'Waterbury Center', 'Websterville',
           'Wolcott', 'Woodbury', 'Wallingford', 'West Pawlet', 'West Rupert', 'West Rutland', 'West Burke',
           'West Charleston', 'West Danville', 'West Glover', 'Weatogue', 'West Granby', 'West Hartland',
           'West Simsbury', 'West Suffield', 'Winchester Center', 'Windsor Locks', 'Winsted', 'Wethersfield',
           'Willimantic', 'Willington', 'Woodstock Valley', 'Wauregan', 'West Mystic', 'West Haven', 'Woodbridge',
           'Washington Depot', 'West Cornwall', 'West Orange', 'Wallington', 'Watchung', 'Wood Ridge', 'Weehawken',
           'West New York', 'Waldwick', 'Wanaque', 'West Milford', 'Wyckoff', 'Woodcliff Lake', 'West Long Branch',
           'Wickatunk', 'Wallpack Center', 'Wharton', 'Whippany', 'Willingboro', 'Waterford Works', 'Wenonah',
           'West Berlin', 'West Creek', 'Westville', 'Winslow', 'Woodbury Heights', 'Woodstown', 'Whitesboro',
           'Wildwood', 'Woodbine', 'West Windsor', 'Wrightstown', 'Waretown', 'Whitehouse', 'Whitehouse Station',
           'Waccabuc', 'White Plains', 'West Harrison', 'Washingtonville', 'West Haverstraw', 'West Nyack',
           'West Point', 'Westtown', 'Whitestone', 'Woodside', 'Woodhaven', 'West Hempstead', 'Westbury',
           'Williston Park', 'Woodmere', 'West Babylon', 'Wading River', 'Wantagh', 'West Islip', 'West Sayville',
           'Wyandanch', 'Wainscott', 'Water Mill', 'Westhampton', 'Westhampton Beach', 'Warnerville', 'Watervliet',
           'West Coxsackie', 'Westerlo', 'West Fulton', 'West Sand Lake', 'Wynantskill', 'Wawarsing', 'West Camp',
           'West Hurley', 'West Kill', 'West Park', 'West Shokan', 'Willow', 'Walden', 'Walker Valley', 'Wallkill',
           'Wappingers Falls', 'Wassaic', 'Wingdale', 'Westbrookville', 'White Lake', 'White Sulphur Springs',
           'Woodbourne', 'Woodridge', 'Wurtsboro', 'Warrensburg', 'Wevertown', 'Whitehall', 'West Chazy',
           'Whippleville', 'Willsboro', 'Witherbee', 'Wampsville', 'Warners', 'Waterloo', 'Weedsport', 'West Monroe',
           'Washington Mills', 'West Burlington', 'Westdale', 'West Eaton', 'West Edmeston', 'Westernville',
           'West Leyden', 'West Winfield', 'Woodgate', 'Wellesley Island', 'Waddington', 'Wanakena', 'West Stockholm',
           'Walton', 'Wells Bridge', 'West Davenport', 'West Oneonta', 'Whitney Point', 'Willet', 'Willseyville',
           'Wales Center', 'West Falls', 'West Valley', 'Wilson', 'Walworth', 'Warsaw', 'Waterport', 'West Bloomfield',
           'West Henrietta', 'Willard', 'Williamson', 'West Clarksville', 'Westons Mills', 'Watkins Glen', 'Waverly',
           'Wellsburg', 'Wellsville', 'Whitesville', 'Woodhull', 'Warrendale', 'West Elizabeth', 'Wexford',
           'West Mifflin', 'Wilmerding', 'Waynesburg', 'West Alexander', 'West Finley', 'Westland', 'West Middletown',
           'Wind Ridge', 'Waltersburg', 'West Leisenring', 'White', 'Wickhaven', 'Wellersburg', 'West Salisbury',
           'Wendel', 'Westmoreland City', 'Whitney', 'Wyano', 'Walston', 'Worthville', 'Weedville', 'Wilcox', 'Wilmore',
           'Windber', 'West Sunbury', 'Wampum', 'West Middlesex', 'West Pittsburg', 'Wheatland', 'Widnoon',
           'West Hickory', 'Wattsburg', 'Waterfall', 'Wells Tannery', 'Westover', 'Wood', 'Wallaceton', 'Warriors Mark',
           'West Decatur', 'Winburne', 'Woodland', 'Woodward', 'Wellsboro', 'Wiconisco', 'Walnut Bottom',
           'Warfordsburg', 'Waynesboro', 'Willow Hill', 'Wrightsville', 'Washington Boro', 'West Willow',
           'Willow Street', 'Witmer', 'Williamsport', 'Watsontown', 'Woolrich', 'Weikert', 'West Milton', 'White Deer',
           'Wilburton', 'Winfield', 'Walnutport', 'Wind Gap', 'Weatherly', 'Waymart', 'White Mills', 'Wapwallopen',
           'White Haven', 'Wilkes Barre', 'Warren Center', 'Wyalusing', 'Wysox', 'Warminster', 'Warrington',
           'Washington Crossing', 'Woxall', 'Wycombe', 'Willow Grove', 'Woodlyn', 'Wyncote', 'Wynnewood', 'Wagontown',
           'West Chester', 'West Grove', 'Wernersville', 'Womelsdorf', 'Winterthur', 'Warrenton',
           'Washington Navy Yard', 'Waldorf', 'Welcome', 'West River', 'Washington Grove', 'Whiteford', 'White Hall',
           'White Marsh', 'Windsor Mill', 'Westernport', 'Wingate', 'Wittman', 'Woolford', 'Worton', 'Wye Mills',
           'Walkersville', 'West Friendship', 'Woodsboro', 'Whaleyville', 'Willards', 'West Mclean', 'WDBG', 'Weems',
           'White Stone', 'Wicomico Church', 'Woodford', 'White Post', 'Wolftown', 'Woodberry Forest', 'Wake',
           'Walkerton', 'Ware Neck', 'Water View', 'Wicomico', 'Woods Cross Roads', 'Wallops Island', 'Wachapreague',
           'Wardtown', 'Wattsville', 'Willis Wharf', 'Withams', 'Warfield', 'Wilsons', 'Wylliesburg', 'Wirtz',
           'Woolwine', 'Weber City', 'Whitetop', 'Wise', 'Willis', 'Woodlawn', 'Wytheville', 'Warm Springs',
           'West Augusta', 'Weyers Cave', 'Wingina', 'Whitewood', 'Wolford', 'Wolfe', 'Welch', 'War', 'Warriormine',
           'Wilcoe', 'Waiteville', 'Wayside', 'Wolfcreek', 'Widen', 'Winifrede', 'Wallback', 'West Columbia',
           'West Hamlin', 'Wharncliffe', 'Wilkinson', 'Wilsondale', 'Winona', 'Wyco', 'White Oak', 'Wheeling',
           'Weirton', 'West Liberty', 'Windsor Heights', 'Walker', 'Webster Springs', 'Whitmer', 'Wallace',
           'West Union', 'Wyatt', 'Wana', 'Wiley Ford', 'Wardensville', 'Walkertown', 'Walnut Cove', 'Woodleaf',
           'Winston Salem', 'Wallburg', 'West End', 'Whitsett', 'Wake Forest', 'Willow Spring', 'Wilsons Mills',
           'Walstonburg', 'Weldon', 'Whitakers', 'Williamston', 'Wanchese', 'Waves', 'Winfall', 'Winton', 'Waco',
           'Wadesboro', 'Waxhaw', 'Wade', 'Wagram', 'Whiteville', 'Winnabow', 'Wrightsville Beach', 'Winterville',
           'Warrensville', 'West Jefferson', 'Wilkesboro', 'Waynesville', 'Weaverville', 'Whittier', 'Warne', 'Wagener',
           'Ward', 'Wedgefield', 'White Rock', 'Whitmire', 'Winnsboro', 'Wellford', 'Woodruff', 'Wadmalaw Island',
           'Walterboro', 'Williams', 'Walhalla', 'Ware Shoals', 'Warrenville', 'Waleska', 'Whitesburg', 'Winston',
           'Wadley', 'Wiley', 'Watkinsville', 'Winder', 'Wrens', 'Warner Robins', 'Warthen', 'Walthourville',
           'Waycross', 'Waresboro', 'West Green', 'Willacoochee', 'Wray', 'Waverly Hall', 'Wellborn', 'White Springs',
           'Welaka', 'Weirsdale', 'Wacissa', 'Wewahitchka', 'Wausau', 'Waldo', 'Worthington Springs', 'Winter Springs',
           'Winter Park', 'Wabasso', 'Winter Beach', 'West Palm Beach', 'Wellington', 'Wesley Chapel', 'Wimauma',
           'Wauchula', 'Winter Haven', 'Winter Garden', 'Windermere', 'Warrior', 'Watson', 'Weogufka', 'West Blocton',
           'Wilsonville', 'West Greene', 'Walnut Grove', 'Wetumpka', 'Weaver', 'Wedowee', 'Webb', 'Whatley', 'Wing',
           'Wagarville', 'Wilmer', 'Wartrace', 'White Bluff', 'White House', 'Whites Creek', 'Whiteside', 'Whitwell',
           'Watauga', 'Walland', 'Wartburg', 'White Pine', 'Wynnburg', 'Woodland Mills', 'Wildersville', 'Westpoint',
           'Walling', 'Whitleyville', 'Walls', 'Walnut', 'Winstonville', 'Wheeler', 'Water Valley', 'Wesson', 'West',
           'Whitfield', 'Waveland', 'Wiggins', 'Walthall', 'Weir', 'Whigham', 'Waddy', 'Willisburg', 'Westview',
           'Waneta', 'Wildie', 'Wallins Creek', 'Warbranch', 'Webbville', 'West Van Lear', 'Wittensville', 'Whick',
           'Wrigley', 'Weeksbury', 'Wendover', 'Wooton', 'West Paducah', 'Wickliffe', 'Wingo', 'Woodburn',
           'West Louisville', 'Wheatcroft', 'West Somerset', 'Whitley City', 'Westerville', 'Washington Court House',
           'West Mansfield', 'Walbridge', 'West Millgrove', 'Wauseon', 'West Unity', 'White Cottage', 'Woodsfield',
           'Walhonding', 'West Lafayette', 'Warnock', 'Wolf Run', 'Williamsfield', 'Willoughby', 'Westlake',
           'Westfield Center', 'Wadsworth', 'West Salem', 'Walnut Creek', 'Winesburg', 'Wooster', 'Wakeman',
           'West Elkton', 'West Alexandria', 'West Manchester', 'Wilberforce', 'West Portsmouth', 'Wellston',
           'Wheelersburg', 'Wilkesville', 'Willow Wood', 'Whipple', 'Wingett Run', 'Wapakoneta', 'Waynesfield',
           'Willshire', 'Wren', 'Whitestown', 'Windfall', 'Waldron', 'Whiteland', 'Wanatah', 'Wheatfield', 'Wakarusa',
           'Winona Lake', 'Wawaka', 'Wolcottville', 'Wolflake', 'Wabash', 'West Middleton', 'Winamac',
           'West College Corner', 'West Baden Springs', 'Westphalia', 'Wadesville', 'West Terre Haute', 'Waynetown',
           'Whitmore Lake', 'Whittaker', 'Wyandotte', 'Walled Lake', 'Wixom', 'West Branch', 'Whittemore',
           'Webberville', 'Weidman', 'White Pigeon', 'White Cloud', 'Walkerville', 'West Olive', 'Walloon Lake',
           'Waters', 'Wolverine', 'Wetmore', 'Watersmeet', 'Watton', 'WDM', 'Waukee', 'West Des Moines', 'What Cheer',
           'Whitten', 'Winterset', 'Wiota', 'Woden', 'Webster City', 'West Bend', 'Woolstock', 'Westgate', 'Washta',
           'Wall Lake', 'Westside', 'Wadena', 'Waucoma', 'Waukon', 'Walford', 'Watkins', 'Wellman', 'Wapello', 'Wever',
           'Walcott', 'Welton', 'Waukesha', 'Whitewater', 'Williams Bay', 'Woodworth', 'Waunakee', 'Wauzeka', 'Woodman',
           'Waupun', 'Wisconsin Dells', 'Wonewoc', 'Wyocena', 'Wausaukee', 'Washington Island', 'Whitelaw', 'Westboro',
           'Wisconsin Rapids', 'Withee', 'Wittenberg', 'Wabeno', 'Warrens', 'Westby', 'Wascott', 'Weyerhaeuser',
           'Winter', 'Waukau', 'Waupaca', 'Wautoma', 'Weyauwega', 'Wild Rose', 'Winnebago', 'Winneconne', 'Willernie',
           'Waconia', 'Wayzata', 'Warba', 'Willow River', 'Wrenshall', 'Wright', 'Wabasha', 'Wanamingo', 'West Concord',
           'Wykoff', 'Waseca', 'Windom', 'Wilmont', 'Willmar', 'Wanda', 'Wheaton', 'Wood Lake', 'Wahkon', 'Waite Park',
           'Waubun', 'White Earth', 'Winger', 'Wolf Lake', 'Wolverton', 'Waskish', 'Wirt', 'Wannaska', 'Warroad',
           'Wakonda', 'Winfred', 'Worthing', 'Waubay', 'Willow Lake', 'Wagner', 'Wessington', 'Wessington Springs',
           'Wolsey', 'Wanblee', 'White River', 'Winner', 'Witten', 'Wakpala', 'Whitehorse', 'Wall', 'Wasta',
           'White Owl', 'Wounded Knee', 'Wahpeton', 'West Fargo', 'Wyndmere', 'Willow City', 'Wimbledon', 'Wishek',
           'Westhope', 'Wildrose', 'Watford City', 'Wilsall', 'Winnett', 'Worden', 'Wyola', 'Wolf Point', 'Whitetail',
           'Wibaux', 'Winifred', 'Whitlash', 'Wolf Creek', 'West Yellowstone', 'Willow Creek', 'Wisdom', 'Wise River',
           'West Glacier', 'Whitefish', 'Waukegan', 'Wauconda', 'Wilmette', 'Winnetka', 'Winthrop Harbor',
           'Wonder Lake', 'Westchester', 'Wasco', 'West Chicago', 'Wood Dale', 'Willow Springs', 'Worth', 'Willowbrook',
           'Waterman', 'Wedron', 'Western Springs', 'Westmont', 'Watseka', 'Woosung', 'Wenona', 'West Brooklyn',
           'Wyanet', 'Wataga', 'Wapella', 'White Heath', 'Walshville', 'Witt', 'Wood River', 'Wrights', 'Walsh',
           'West York', 'Waggoner', 'Woodson', 'Walnut Hill', 'Waltonville', 'Wayne City', 'West Frankfort',
           'Whittington', 'Willisville', 'Wentzville', 'West Alton', 'Wright City', 'Wyaconda', 'Winigan', 'Wardell',
           'Whiteoak', 'Wolf Island', 'Wappapello', 'Weatherby', 'Webb City', 'Wooldridge', 'Whiteman Air Force Base',
           'Wesco', 'Walnut Shade', 'Wasola', 'Weaubleau', 'West Plains', 'Windyville', 'Wathena', 'Welda', 'Wamego',
           'West Mineral', 'White City', 'Wilsey', 'Webber', 'Wichita', 'Wakeeney', 'Woodston', 'Weskan', 'Wahoo',
           'Walthill', 'Weeping Water', 'Western', 'Wilber', 'Wymore', 'Wausa', 'Winnetoon', 'Winside', 'Wisner',
           'Wynot', 'Wolbach', 'Wauneta', 'Willow Island', 'Whiteclay', 'Westwego', 'Welsh', 'Weyanoke', 'White Castle',
           'Waterproof', 'Wildsville', 'Winnfield', 'Wilmar', 'Whelen Springs', 'Wickes', 'Wabbaseka', 'Wilburn',
           'West Memphis', 'West Helena', 'West Ridge', 'Wheatley', 'Widener', 'Wynne', 'Waldenburg', 'Walnut Ridge',
           'Weiner', 'Williford', 'Wideman', 'Wiseman', 'Western Grove', 'Witts Springs', 'West Fork', 'Witter',
           'Weatherford', 'Wapanucka', 'Walters', 'Waurika', 'Wakita', 'Watonga', 'Waukomis', 'Waynoka', 'Wann',
           'Wynona', 'Wagoner', 'Wainwright', 'Webbers Falls', 'Welling', 'Wardville', 'Wanette', 'Weleetka', 'Wetumka',
           'Wewoka', 'Watts', 'Wister', 'Wylie', 'Waxahachie', 'Wills Point', 'Whitewright', 'Wolfe City', 'Waskom',
           'Woodlake', 'Wiergate', 'Wichita Falls', 'Weinert', 'Windthorst', 'Whitt', 'Walnut Springs', 'Wortham',
           'Woodway', 'Waller', 'Wallis', 'Wallisville', 'Winnie', 'Wheelock', 'Weesatche', 'Westhoff', 'Waring',
           'Weslaco', 'Walburg', 'Wimberley', 'Wrightsboro', 'Waelder', 'Warda', 'Weimar', 'Waka', 'Wildorado',
           'Whiteface', 'Whitharral', 'Wolfforth', 'Winters', 'Wickett', 'Wink', 'WBAMC', 'Wheat Ridge', 'Weldona',
           'Woodrow', 'Wild Horse', 'Woodland Park', 'Walsenburg', 'Westcliffe', 'Woody Creek', 'Wamsutter', 'Worland',
           'Wapiti', 'Wolf', 'Wyarno', 'Wayan', 'Weippe', 'White Bird', 'Weiser', 'Worley', 'West Jordan', 'WJ',
           'Wallsburg', 'Whiterocks', 'Woods Cross', 'Winkelman', 'Waddell', 'Wellton', 'Wenden', 'Wickenburg',
           'Wikieup', 'Wittmann', 'Willcox', 'White Mountain Lake', 'Whiteriver', 'Willow Beach', 'Window Rock',
           'Waterflow', 'Wagon Mound', 'Watrous', 'White Sands Missile Range', 'Whites City', 'Weed', 'Winnemucca',
           'Washoe Valley', 'West Wendover', 'WLA', 'West Hollywood', 'West Hills', 'Westlake Village',
           'Woodland Hills', 'West Covina', 'Warner Springs', 'Westmorland', 'Winterhaven', 'Wrightwood', 'Wildomar',
           'Waukena', 'Wofford Heights', 'Woody', 'Wishon', 'Woodacre', 'Watsonville', 'Wilseyville', 'Westley',
           'Willits', 'Witter Springs', 'Weott', 'Whitethorn', 'West Sacramento', 'Willows', 'Whiskeytown', 'Whitmore',
           'Waikoloa', 'Wahiawa', 'Waialua', 'Waianae', 'Wailuku', 'Waimanalo', 'Waimea', 'Waipahu',
           'Wheeler Army Airfield', 'Wake Island', 'Welches', 'West Linn', 'Waldport', 'Willamina', 'Walterville',
           'Wedderburn', 'Westfir', 'Wilbur', 'Wilderville', 'Wallowa', 'Westfall', 'Woodinville', 'Wauna', 'Wilkeson',
           'Winlock', 'Wahkiacus', 'Washougal', 'White Salmon', 'Wishram', 'Wenatchee', 'Warden', 'Wilson Creek',
           'Wapato',
           'White Swan', 'Wellpinit', 'West Richland', 'Waitsburg', 'Walla Walla', 'Wallula', 'Washtucna', 'Wasilla',
           'White Mountain', 'Ward Cove', 'Wrangell']
XCities = ['Xenia']
YCities = ['Yauco', 'Yabucoa', 'Yarmouth Port', 'York', 'York Beach', 'York Harbor', 'Yarmouth', 'Yantic',
           'Yorktown Heights', 'Yonkers',
           'Yaphank', 'Youngsville', 'Yulan', 'Yorkville', 'Yorkshire', 'Youngstown', 'Youngwood', 'Yukon', 'Yatesboro',
           'Yeagertown', 'York Haven', 'York New Salem', 'York Springs', 'Yorklyn', 'Yorktown', 'Yale', 'Yawkey',
           'Yolyn', 'Yellow Spring', 'Yadkinville', 'Yanceyville', 'Yemassee', 'Young Harris', 'Yatesville', 'Yulee',
           'Yankeetown', 'Yalaha', 'Yuma', 'Yazoo City', 'Yeaddiss', 'Yerkes', 'Yosemite', 'Yellow Springs', 'Yoder',
           'Young America', 'Yeoman', 'Ypsilanti', 'Yankton', 'Yates City', 'Yates Center', 'Yutan', 'Yellville',
           'Yantis', 'Yoakum', 'Yancey', 'Yampa', 'Yellow Jacket', 'Yellowstone National Park', 'Yellow Pine',
           'Yarnell', 'Youngtown', 'YPG', 'Young', 'Yucca', 'Yatahey', 'Yeso', 'Yerington', 'Yucca Valley', 'Yermo',
           'Yucaipa', 'Yorba Linda', 'Yettem', 'Yountville', 'Yosemite National Park',
           'Yuba City', 'Yreka', 'Yigo', 'Yap', 'Yamhill', 'Yachats', 'Yoncalla', 'Yelm', 'Yacolt', 'Yakima', 'Yakutat']
ZCities = ['Zarephath', 'Zelienople', 'Zullinger', 'Zion Grove', 'Zionsville', 'Zionhill', 'Zieglerville', 'Zacata',
           'Zuni', 'Zebulon',
           'Zionville', 'Zirconia', 'Zellwood', 'Zephyrhills', 'Zolfo Springs', 'Zoe', 'Zanesfield', 'Zanesville',
           'Zoar', 'Zaleski', 'Zeeland',
           'Zearing', 'Zwingle', 'Zenda', 'Zachow', 'Zimmerman', 'Zumbro Falls', 'Zumbrota', 'Zap', 'Zahl', 'Zortman',
           'Zurich', 'Zion',
           'Zeigler', 'Zalma', 'Zanoni', 'Zachary', 'Zwolle', 'Zavalla', 'Zephyr', 'Zapata', 'Zephyr Cove', 'Zenia',
           'Zamora', 'Zillah']
tweetTextArray = []

USStates = ['Alabama',
            'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
            'Hawaii', 'Idaho', 'Illinois', 'Indiana',
            'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
            'Mississippi', 'Missouri', 'Montana',
            'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico''New York', 'North Carolina',
            'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
            'South Dakota', 'Tennessee', 'Texas',
            'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
stateAbbreviations = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN',
                      'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                      'NM', 'NY', 'NC', 'ND', 'OH', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA',
                      'WV', 'WI', 'WY', 'GU', 'PR', 'VI', 'DC']
cityNicknames = ['Big Apple', 'City that Never Sleeps', 'City of Angels', 'Windy City', 'Chitown', 'Space City',
                 'City of Brotherly Love', 'Alamo City',
                 'Motown', 'Hockeytown', 'Motor City', 'Sin City', 'Charm City', 'Little Cuba', 'Steel City',
                 'Mile High City', 'Hotlanta', 'Big Easy', 'NOLA',
                 'Twin Cities', 'Oaktown', 'Emerald City', 'Brew Town', 'Big D', 'Emerald City', 'NYC', 'LA', 'SF']
countryList = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola',
               'Anguilla', 'Antigua & Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia',
               'Austria', 'Azerbaijan', 'The Bahamas', 'Bahrain', 'Bangladesh', 'Barbados',
               'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia & Herzegovina',
               'Botswana', 'Brazil', 'British Virgin Is.', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burma', 'Burundi',
               'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Rep.', 'Chad',
               'Chile', 'China',
               'Colombia', 'Comoros', '"Congo, Dem. Rep.', 'Congo, Repub. of the', 'Cook Islands', 'Costa Rica',
               'Cote d''Ivoire',
               'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
               'East Timor',
               'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia',
               'Faroe Islands', 'Fiji', 'Finland',
               'France', 'French Guiana', 'French Polynesia', 'Gabon', 'The Gambia', 'Gaza Strip', 'Georgia', 'Germany',
               'Ghana', 'Gibraltar',
               'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea',
               'Guinea-Bissau', 'Guyana', 'Haiti',
               'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland',
               'Isle of Man', 'Israel', 'Italy',
               'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'North Korea', 'South Korea',
               'Kuwait', 'Kyrgyzstan',
               'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg',
               'Macau', 'Macedonia', 'Madagascar',
               'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania',
               'Mauritius', 'Mayotte', 'Mexico',
               'Micronesia, Fed. St.', 'Moldova', 'Monaco', 'Mongolia', 'Montserrat', 'Morocco', 'Mozambique',
               'Namibia', 'Nauru', 'Nepal', 'Netherlands',
               'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
               'N. Mariana Islands', 'Norway', 'Oman', 'Pakistan',
               'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal',
               'Puerto Rico', 'Qatar', 'Reunion', 'Romania',
               'Russia', 'Rwanda', 'Saint Helena', 'Saint Kitts & Nevis', 'Saint Lucia', 'St Pierre & Miquelon',
               'Saint Vincent and the Grenadines', 'Samoa',
               'San Marino', 'Sao Tome & Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone',
               'Singapore', 'Slovakia', 'Slovenia',
               'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland',
               'Sweden', 'Switzerland', 'Syria', 'Taiwan',
               'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad & Tobago', 'Tunisia', 'Turkey',
               'Turkmenistan', 'Turks & Caicos Is', 'Tuvalu',
               'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan',
               'Vanuatu', 'Venezuela', 'Vietnam',
               'Virgin Islands', 'Wallis and Futuna', 'West Bank', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']

ckey = 'XmGJg5YuU4bS8F8LdUoCTxPSp'
csecret = 'B4Bp2xVhPz7HZC3O71CmcvFo57k7l6ToTEhT3Aewi3srqqCWrG'
atoken = '2456534122-xGxnlevtZHSW3ZMhXV1s8l7obR1hCPfVHzS8Aiw'
asecret = '4A87PvxzdzxqTuvoWdLZqHIkW6KtcEWIHAHrJx0T5xEPf'
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth, wait_on_rate_limit=True)


class TweetEncode:

    def cityValidate(self, txt):
        firstLetter = txt[0]
        if firstLetter is 'A' or firstLetter is 'a':
            cityList = ACities
        elif firstLetter is 'B' or firstLetter is 'b':
            cityList = BCities
        elif firstLetter is 'C' or firstLetter is 'c':
            cityList = CCities
        elif firstLetter is 'D' or firstLetter is 'd':
            cityList = DCities
        elif firstLetter is 'E' or firstLetter is 'e':
            cityList = ECities
        elif firstLetter is 'F' or firstLetter is 'f':
            cityList = FCities
        elif firstLetter is 'G' or firstLetter is 'g':
            cityList = GCities
        elif firstLetter is 'H' or firstLetter is 'h':
            cityList = HCities
        elif firstLetter is 'I' or firstLetter is 'i':
            cityList = ICities
        elif firstLetter is 'J' or firstLetter is 'j':
            cityList = JCities
        elif firstLetter is 'K' or firstLetter is 'k':
            cityList = KCities
        elif firstLetter is 'L' or firstLetter is 'k':
            cityList = LCities
        elif firstLetter is 'M' or firstLetter is 'm':
            cityList = MCities
        elif firstLetter is 'N' or firstLetter is 'n':
            cityList = NCities
        elif firstLetter is 'O' or firstLetter is 'n':
            cityList = OCities
        elif firstLetter is 'P' or firstLetter is 'p':
            cityList = PCities
        elif firstLetter is 'Q' or firstLetter is 'q':
            cityList = QCities
        elif firstLetter is 'R' or firstLetter is 'r':
            cityList = RCities
        elif firstLetter is 'S' or firstLetter is 's':
            cityList = SCities
        elif firstLetter is 'T' or firstLetter is 't':
            cityList = TCities
        elif firstLetter is 'U' or firstLetter is 'u':
            cityList = UCities
        elif firstLetter is 'V' or firstLetter is 'v':
            cityList = VCities
        elif firstLetter is 'W' or firstLetter is 'w':
            cityList = WCities
        elif firstLetter is 'X' or firstLetter is 'x':
            cityList = XCities
        elif firstLetter is 'Y' or firstLetter is 'y':
            cityList = YCities
        elif firstLetter is 'Z' or firstLetter is 'z':
            cityList = ZCities
        else:
            cityList = []
        choice = 0
        for items in cityList:
            if txt == items:
                choice = 10
        return choice

    def internationalValidate(self, txt):
        found = 0
        for country in countryList:
            if txt == country:
                found = 5
        return found

    def AbbreviationStateValidate(self, Userstate):
        found = 0
        for state in stateAbbreviations:
            if Userstate == state:
                found = 5
        return found

    def fullStateValidate(self, state):
        found = 0
        for items in USStates:
            if state == items:
                found = 10
        return found

    def nicknameValidate(self, state):
        found = 0
        for items in cityNicknames:
            if state == items:
                found = 10
        return found

    def locationController(self, location):
        selection = 9
        location = str(location).replace("'", "").replace('"', "")
        if (location == ''):
            selection = 0
        if (selection == 9):
            if (location.count('USA') >= 1 or location.count('United States') >= 1 or location.count(
                    'U.S.A') >= 1 or location.count('Estados Unidos') >= 1):
                selection = 1
            if (',' in location and selection == 9):
                split = location.split(',')
                city = split[0]
                state = split[1].strip(' ')

                if (len(state) == 2):
                    stateValidate = self.AbbreviationStateValidate(state)
                    cityValidation = self.cityValidate(city)
                    if (stateValidate and cityValidation != 0):
                        # City and abbreviated state
                        selection = 2

                    else:
                        stateValidate = self.fullStateValidate(state)
                        cityValidation = self.cityValidate(city)
                        internationalValidate = self.internationalValidate(state)
                        if (stateValidate and cityValidation != 0):
                            selection = 3
                        elif (internationalValidate != 0):
                            selection = 7
                        else:
                            selection = 9
            elif (selection == 9):
                newcityValidation = self.cityValidate(location)
                if (newcityValidation != 0):
                    selection = 4
                stateValidate = self.fullStateValidate(location)
                if (stateValidate != 0):
                    selection = 5
                nickNameValidation = self.nicknameValidate(location)
                if (nickNameValidation != 0):
                    selection = 6
                internationalValidate = self.internationalValidate(location)
                if (internationalValidate != 0):
                    selection = 7
                if (selection == -1):
                    selection = 9
        return selection

    def verifiedValidate(self, verified):
        verified = str(verified)
        verification = -1
        if verified == "True":
            verification = 1
        elif verified == '0':
            verification = 0
        elif verified == 'False':
            verification = 0
        return verification

    def tweetLang(self, language):
        selection = -1
        if (language == 'en'):
            selection = 0
        elif (language == 'en-gb'):
            selection = 1
        elif (language == 'de'):
            selection = 2
        elif (language == 'es'):
            selection = 3
        elif (language == 'ru'):
            selection = 4
        elif (language == 'id'):
            selection = 5
        elif (language == 'zh-cn'):
            selection = 6
        elif (language == 'pt'):
            selection = 7
        elif (language == 'ar'):
            selection = 8
        elif (language == 'tr'):
            selection = 9
        elif (language == 'tl'):
            selection = 10
        elif (language == 'ta'):
            selection = 11
        elif (language == 'ro'):
            selection = 12
        elif (language == 'pl'):
            selection = 13
        elif (language == 'lt'):
            selection = 14
        elif (language == 'ja'):
            selection = 15
        elif (language == 'it'):
            selection = 16
        elif (language == 'in'):
            selection = 17
        elif (language == 'ht'):
            selection = 18
        elif (language == 'hi'):
            selection = 19
        elif (language == 'fr'):
            selection = 20
        elif (language == 'et'):
            selection = 21
        elif (language == 'ca'):
            selection = 22
        elif (language == 'sv'):
            selection = 24
        elif (language == 'no'):
            selection = 25
        elif (language == 'nl'):
            selection = 26
        elif (language == 'is'):
            selection = 27
        elif (language == 'hu'):
            selection = 28
        elif (language == 'fi'):
            selection = 29
        elif (language == 'eu'):
            selection = 30
        elif (language == 'da'):
            selection = 31
        elif (language == 'cy'):
            selection = 32
        elif (language == 'cs'):
            selection = 33
        elif (language == 'und'):
            selection = 34
        else:
            selection = 35
        return selection

    def accountLang(self, language):
        selection = -1
        if (language == 'en'):
            selection = 0
        elif (language == 'en-gb'):
            selection = 1
        elif (language == 'de'):
            selection = 2
        elif (language == 'es'):
            selection = 3
        elif (language == 'ru'):
            selection = 4
        elif (language == 'id'):
            selection = 5
        elif (language == 'zh-cn'):
            selection = 6
        elif (language == 'pt'):
            selection = 7
        elif (language == 'ar'):
            selection = 8
        elif (language == 'tr'):
            selection = 9
        elif (language == 'tl'):
            selection = 10
        elif (language == 'ta'):
            selection = 11
        elif (language == 'ro'):
            selection = 12
        elif (language == 'pl'):
            selection = 13
        elif (language == 'lt'):
            selection = 14
        elif (language == 'ja'):
            selection = 15
        elif (language == 'it'):
            selection = 16
        elif (language == 'in'):
            selection = 17
        elif (language == 'ht'):
            selection = 18
        elif (language == 'hi'):
            selection = 19
        elif (language == 'fr'):
            selection = 20
        elif (language == 'et'):
            selection = 21
        elif (language == 'ca'):
            selection = 22
        elif (language == 'sv'):
            selection = 24
        elif (language == 'no'):
            selection = 25
        elif (language == 'nl'):
            selection = 26
        elif (language == 'is'):
            selection = 27
        elif (language == 'hu'):
            selection = 28
        elif (language == 'fi'):
            selection = 29
        elif (language == 'eu'):
            selection = 30
        elif (language == 'da'):
            selection = 31
        elif (language == 'cy'):
            selection = 32
        elif (language == 'cs'):
            selection = 33
        elif (language == 'und'):
            selection = 34
        elif (selection == -1):
            selection = 35
        return selection

    def encodeDevice(self, text):
        print(text)
        text = str(text).lstrip()
        selection = -1
        if text == 'Twitter for Web':
            selection = 0
        elif text == 'Twitter Web Client':
            selection = 1
        elif text == 'Twitter for Android':
            selection = 2
        elif text == 'Twitter for iPad':
            selection = 3
        elif text == 'Twitter for iPhone':
            selection = 3
        elif text == 'Periscope':
            selection = 5
        elif text == 'Twitter Web App':
            selection = 6
        elif text == 'Twitter Media Studio':
            selection = 7
        elif text == 'Tweetdeck':
            selection = 8
        elif text == 'Facebook':
            selection = 9
        elif text == 'Instagram':
            selection = 10
        elif text == 'TweetDeck':
            selection = 11
        elif text == 'IFTTT':
            selection = 12
        elif text == 'Hootsuite Inc.':
            seletion = 13
        elif text == 'Tweedle':
            selection = 13
        elif text == 'LinkedIn':
            selection = 14
        elif(selection==-1):
            selection = 15
        print(selection)
        return selection

    def tweetHashtagCount(self, tweet):
        tweet = str(tweet)
        hashtagCount = tweet.count('#')
        return hashtagCount

    def tweetTaggedCount(self, tweetText):
        tweet = str(tweetText)
        taggedCount = tweet.count('@')
        return taggedCount

    def tweetEmojiCount(self, tweetText):
        tweet = str(tweetText)
        emojiCount = ''.join(c for c in tweet if c in emoji.UNICODE_EMOJI)
        numEmojiCount = len(emojiCount)
        return numEmojiCount

    def differenceFirstTweetAccountCreation(self, firstTweetDate, accountCreationDate):
        print(firstTweetDate)
        print(accountCreationDate)

    def tweetWordCount(self, tweetText):
        tweet = str(tweetText)
        count = 1
        for letter in tweet:
            if letter == " ":
                count = count + 1
        return count

    def profileHashtagCount(self, profileDescription):
        profileDescription = str(profileDescription)
        hashtagCount = profileDescription.count('#')
        return hashtagCount

    def profileTagCount(self, profileDescription):
        stringDesc = str(profileDescription)
        tagCount = stringDesc.count('@')
        return tagCount

    def profileEmojiCount(self, profileDescription):
        stringDesc = str(profileDescription)
        emojiCount = ''.join(c for c in stringDesc if c in emoji.UNICODE_EMOJI)
        numEmojiCount = len(emojiCount)
        return numEmojiCount

    def tweetLinkCount(self, tweet):
        tweet = str(tweet)
        linkCount = tweet.count('http')
        return linkCount

    def encodeInput(self, userHandles, tweetTexts):
        main_df = pd.read_csv("mattTest.tsv", sep='\t')
        i = 0
        finalEncodedList = []
        while (i < len(main_df.index)):
            current_row = main_df.iloc[[i]]
            currentLocation = current_row.loc[:, 'UserLocation'].values[0]
            if (currentLocation != ''):
                currentLocation = current_row.loc[:, 'UserLocation'].values[0]
            else:
                currentLocation = 'N/A'
            accountDescription = current_row.loc[:, 'UserDescription'].values[0]
            accountLanguage = current_row.loc[:, 'AccountLanguage'].values[0]
            tweetLanguage = current_row.loc[:, 'TweetLanguage'].values[0]
            tweetText = current_row.loc[:, 'TweetText'].values[0]
            tweetTextArray.append(tweetText)
            tweetClient = current_row.loc[:, 'TweetClient'].values[0]
            #accountCreationDate = current_row.loc[:]
            isVerified = current_row.loc[:, 'isVerified'].values[0]
            # isMalicious = current_row.loc[:, 'isMalicious'].values[0]

            locationEncode = self.locationController(currentLocation)
            descriptionHashtags = self.profileHashtagCount(accountDescription)
            descriptionTags = self.profileTagCount(accountDescription)
            descriptionEmojis = self.profileEmojiCount(accountDescription)
            accountLanguageEncode = self.accountLang(accountLanguage)
            tweetLanguageEncode = self.tweetLang(tweetLanguage)
            tweetTextHashtagCount = self.tweetHashtagCount(tweetText)
            tweetTaggedUserCount = self.tweetTaggedCount(tweetText)
            #tweetWordCount = self.tweetWordCount(tweetText)
            tweetEmojiCount = self.tweetEmojiCount(tweetText)
            tweetURLCount = self.tweetLinkCount(tweetText)
            print('Tweet Client:', tweetClient)
            tweetClientEncode = self.encodeDevice(tweetClient)
            isVerifiedEncode = self.verifiedValidate(isVerified)

            # isMalicious = 1
            encodedRow = [locationEncode, descriptionHashtags, descriptionTags, descriptionEmojis,
                          accountLanguageEncode, tweetLanguageEncode, tweetTextHashtagCount,
                          tweetURLCount, tweetTaggedUserCount, tweetEmojiCount, tweetClientEncode,
                          isVerifiedEncode]
            finalEncodedList.append(encodedRow)
            i = i + 1
        finalList = pd.DataFrame(finalEncodedList)
        # finalList.to_csv('EncodedTweetsApril6.tsv', sep='\t')
        runModels = ModelTest(finalList, userHandles, tweetTexts)


class ModelTest():

    def DecisionTreeMethod(self, encodedInput):
        filename = 'SciKitModels/decisionTreeModel.sav'
        loaded_model = load(filename)
        result = loaded_model.predict(encodedInput)
        return result

    def KNeighborsMethod(self, encodedInput):
        filename = 'SciKitModels/KNeighborsModel.sav'
        loaded_model = load(filename)
        result = loaded_model.predict(encodedInput)
        return result

    def SVCMethod(self, encodedInput):
        filename = 'SciKitModels/SVCModel.sav'
        loaded_model = load(filename)
        result = loaded_model.predict(encodedInput)
        return result

    def RandomForestMethod(self, encodedInput):
        filename = 'SciKitModels/RandomForestModel.sav'
        loaded_model = load(filename)
        result = loaded_model.predict(encodedInput)
        return result

    def GradientBoostModel(self, encodedInput):
        filename = 'SciKitModels/GradientModel.sav'
        loaded_model = load(filename)
        result = loaded_model.predict(encodedInput)
        return result

    def __init__(self, encodedInput, userHandles, tweetTexts):
        self.encodedInput = encodedInput
        self.userHandles = userHandles
        self.tweetTexts = tweetTexts
        self.MachineLearningController(encodedInput, tweetTexts, userHandles)

    def MachineLearningController(self, encodedInput, tweetTexts, userHandles):
        decisionTreeResults = self.DecisionTreeMethod(encodedInput)
        kNeighborsResults = self.KNeighborsMethod(encodedInput)
        SVCResults = self.SVCMethod(encodedInput)
        randomForestResults = self.RandomForestMethod(encodedInput)
        gradientBoostResults = self.GradientBoostModel(encodedInput)
        self.algoVote(decisionTreeResults, kNeighborsResults, SVCResults, randomForestResults, gradientBoostResults,
                      tweetTexts, userHandles)

    def algoVote(self, decisionTree, kNeighbors, SVC, randomForest, gradientBoostResults, tweetTexts, userHandles):
        i = 0
        averageList = []
        scoreList = []
        while i < len(decisionTree):
            treeItem = decisionTree[i]
            kNeighborsItem = kNeighbors[i]
            svcItem = SVC[i]
            forestItem = randomForest[i]
            gradientBoostItem = gradientBoostResults[i]
            total = (treeItem + kNeighborsItem + svcItem + forestItem + gradientBoostItem)
            totalAverage = total / 5
            i = i + 1
            averageList.append(totalAverage)
        averagedTotal = np.mean(averageList)
        averagedTotal = round(averagedTotal, 2) * 100
        if(averagedTotal < 10.0):
            averagedTotal = 0.0
        displayResults(averagedTotal, averageList, userHandles, tweetTexts)
        print('Account Score: ', averagedTotal)
        print(tweetTexts)
        print(userHandles)
        print(averageList)


class TweetGetter():

    def handleTest(self):
        handle = input("Enter a twitter handle to find illegitimate tweets: \n")
        testTweet = tweepy.Cursor(api.user_timeline, tweet_mode='extended', id=handle, count=200).items(150)
        with open('mattTest.tsv', 'a') as csvFile:
            header = ['UserLocation', 'UserDescription', 'AccountLanguage', 'TweetLanguage', 'TweetText', 'TweetClient',
                      'isVerified']
            writer = csv.writer(csvFile, delimiter='\t')
            writer.writerow(header)
            csvFile.close()

        i = 0
        for tweet in testTweet:
            row = []
            user = tweet.user
            # UserLocation
            userLocation = tweet.user.location
            row.append(userLocation)
            # UserDescription
            userDescription = tweet.user.description
            if (userDescription == ''):
                userDescription = 'N/A'
            row.append(userDescription)
            userLang = tweet.user.lang
            row.append(userLang)
            # TweetLanguage
            tweetLang = tweet.lang
            row.append(tweetLang)
            #AccountCreationDate
            accountCreation = tweet.user.created_at
            firstTweetDate = tweet.user
            # TweetText
            tweetText = tweet.full_text
            row.append(tweetText)
            # TweetClientName
            tweetSource = tweet.source
            row.append(tweetSource)
            isVerified = tweet.user.verified
            row.append(isVerified)
            i = i + 1

            with open('mattTest.tsv', 'a') as csvFile:
                writer = csv.writer(csvFile, delimiter='\t')
                writer.writerow(row)
                csvFile.close()
        print(i, " tweets added to CSV file!")
        run = TweetEncode()
        run.encodeInput()

    def searchQuery(self, text):
        raw_query = text
        print(raw_query)
        with open('mattTest.tsv', 'w') as csvFile:
            row = ['UserLocation', 'UserDescription', 'AccountLanguage', 'TweetLanguage', 'TweetText', 'TweetClient',
                   'isVerified']
            writer = csv.writer(csvFile, delimiter='\t')
            writer.writerow(row)
            csvFile.close()
        queryTweets = tweepy.Cursor(api.search, q=raw_query, tweet_mode='extended', result_type="recent",
                                    lang="en").items(250)
        x = 0
        userHandles = []
        tweetTexts = []
        while x < 250:
            for tweet in queryTweets:
                row = []
                # UserLocation
                userHandle = tweet.user.screen_name
                userHandles.append(userHandle)
                # UserLocation
                userLocation = tweet.user.location
                if (userLocation == ''):
                    row.append('N/A')
                else:
                    row.append(userLocation)
                # UserDescription
                userDescription = tweet.user.description
                if (userDescription == ''):
                    row.append('N/A')
                else:
                    row.append(userDescription)
                userLang = tweet.user.lang
                row.append(userLang)
                # TweetLanguage
                tweetLang = tweet.lang
                row.append(tweetLang)
                # TweetText
                tweetText = tweet.full_text
                tweetTexts.append(tweetText)
                row.append(tweetText)
                # TweetClientName
                tweetSource = tweet.source
                row.append(tweetSource)
                isVerified = tweet.user.verified
                row.append(isVerified)

                with open('mattTest.tsv', 'a') as csvFile:
                    writer = csv.writer(csvFile, delimiter='\t')
                    writer.writerow(row)
                    csvFile.close()
            x = x + 1

        run = TweetEncode()
        run.encodeInput(userHandles, tweetTexts)

    def timelineScan(self, handle):
        testTweet = tweepy.Cursor(api.user_timeline, tweet_mode='extended', id=handle, count=200).items(150)
        with open('mattTest.tsv', 'w') as csvFile:
            header = ['UserLocation', 'UserDescription', 'AccountLanguage', 'TweetLanguage', 'TweetText', 'TweetClient',
                      'isVerified']
            writer = csv.writer(csvFile, delimiter='\t')
            writer.writerow(header)
            csvFile.close()
        i = 0
        userHandles = []
        tweetTexts = []
        for tweet in testTweet:
            row = []
            # UserLocation
            userHandle = tweet.user.screen_name
            userHandles.append(userHandle)
            userLocation = tweet.user.location
            row.append(userLocation)
            # UserDescription
            userDescription = tweet.user.description
            if (userDescription == ''):
                userDescription = 'N/A'
            row.append(userDescription)
            userLang = tweet.user.lang
            row.append(userLang)
            # TweetLanguage
            tweetLang = tweet.lang
            row.append(tweetLang)
            # TweetText
            tweetText = tweet.full_text
            row.append(tweetText)
            tweetTexts.append(tweetText)
            # TweetClientName
            tweetSource = tweet.source
            row.append(tweetSource)
            isVerified = tweet.user.verified
            row.append(isVerified)
            i = i + 1

            with open('mattTest.tsv', 'a') as csvFile:
                writer = csv.writer(csvFile, delimiter='\t')
                writer.writerow(row)
                csvFile.close()
        print(i, " tweets added to CSV file!")
        run = TweetEncode()
        run.encodeInput(userHandles, tweetTexts)


accountOrQuery = 1

#UI Code
def setUpAccount():
    global accountOrQuery
    accountOrQuery = 1
    if (textBox.get() == 'Enter a Search Query...'):
        textBox.delete(0, "end")
        textBox.insert(0, 'Enter a Twitter Handle...')
    elif (textBox.get() == 'Enter a Twitter Handle...'):
        textBox.delete(0, "end")


def setUpQuery():
    global accountOrQuery
    accountOrQuery = 0
    if (textBox.get() == 'Enter a Twitter Handle...'):
        textBox.delete(0, "end")
        textBox.insert(0, 'Enter a Search Query...')
    else:
        textBox.insert(0, 'Enter a Search Query...')


def on_entry_click(event):
    textBox.delete(0, "end")  # delete all the text in the entry


def startSearch(text, accountorquery):
    tweetPull = TweetGetter()
    if (accountorquery == 0):
        print('Query', text)
        tweetPull.searchQuery(text)
    elif (accountorquery == 1):
        print('Account', text)
        tweetPull.timelineScan(text)


def displayResults(averagedTotal, averageList, userHandles, tweetTexts):
    scoreString = 'Likelihood of Malicious Activity: ' + str(averagedTotal) + '/100'
    score.set(scoreString)

    listBoxUsers.delete('0', 'end')
    listBoxTweets.delete('0', 'end')
    listBoxAverage.delete('0', 'end')
    for user in userHandles:
        listBoxUsers.insert(END, user)
        listBoxUsers.insert(END, '')
    listBoxUsers.pack(side='left', fill='y')

    for tweet in tweetTexts:
        line = ''.join(i for i in tweet if ord(i) < 128)
        listBoxTweets.insert(END, line)
        listBoxTweets.insert(END, '')
    listBoxTweets.pack(side='left', fill='y')

    for average in averageList:
        averageString = str(average)
        listBoxAverage.insert(END, averageString)
        listBoxAverage.insert(END, '')
    listBoxAverage.pack(side='left', fill='y')


root = tkinter.Tk()
root.title('Identifying Disinformation on Twitter')
root.geometry('700x500')
root.config(height=2000, width=1000)
img = tkinter.PhotoImage(file='Logo.png')
image = tkinter.Label(image=img).pack()
instructions = tkinter.StringVar()
instructions.set('Enter a handle: ')
label_1 = Label(root, text="Scan for Disinformation on: ")
label_1.pack()
label_1.config(font=('Helvetica Neue', 25))
AccountButton = Radiobutton(root, text="A Twitter User", command=lambda: setUpAccount(), value=1, variable=1)
AccountButton.pack(padx=0, pady=0)
QueryButton = Radiobutton(root, text="A Search Query", value=2, variable=1, command=lambda: setUpQuery())
QueryButton.pack(padx=0, pady=0)
textBox = Entry(root, width=40)
textBox.insert(0, 'Enter a Twitter Handle...')
textBox.bind('<FocusIn>', on_entry_click)
textBox.pack()



listBoxTweets = tkinter.Listbox(root, background="#00aced", fg="white", width=120)
listBoxUsers = tkinter.Listbox(root, background="#00aced", fg="white", width=15)
listBoxAverage = tkinter.Listbox(root, background="#00aced", fg="white", width=15)

def yview(*args):
    listBoxAverage.yview(*args)
    listBoxUsers.yview(*args)
    listBoxTweets.yview(*args)


def OnVsb(*args):
    listBoxUsers.yview(*args)
    listBoxTweets.yview(*args)
    listBoxAverage.yview(*args)

def OnMouseWheel(event):
    listBoxUsers.yview("scroll", event.delta,"units")
    listBoxAverage.yview("scroll",event.delta,"units")
    listBoxTweets.yview("scroll",event.delta,"units")

    # this prevents default bindings from firing, which
    # would end up scrolling the widget twice
    return "break"


def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    startSearch(value, 1)
    print('You selected item %d: "%s"' % (index, value))
    print(value)
    textBox.delete('0', 'end')
    textBox.insert('0', value)

scrollbar = tkinter.Scrollbar(root, orient='vertical', command=OnVsb())
scrollbar.pack(side='right', fill='y')
listBoxTweets.config(yscrollcommand=scrollbar.set)
listBoxUsers.config(yscrollcommand=scrollbar.set)
listBoxAverage.config(yscrollcommand=scrollbar.set)
listBoxTweets.bind("<MouseWheel>", OnMouseWheel)
listBoxUsers.bind("<MouseWheel>", OnMouseWheel)
listBoxAverage.bind("<MouseWheel>", OnMouseWheel)
listBoxUsers.bind('<<ListboxSelect>>', onselect)

button = Button(root, text="Submit", command=lambda: startSearch(str(textBox.get()), accountOrQuery))
button.pack()
score = tkinter.StringVar()
score.set('Likelihood of Malicious Activity: ')
label_3 = Label(root, textvariable=score)
label_3.pack()
label_3.config(font=('Helvetica Neue', 20))

root.mainloop()
