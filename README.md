3번째 과제
=========

python을 이용해서 지니뮤직의 top50의 노래제목과 가수를 크롤링했다.
>crawling을 하기 위해 python의 라이브러리인 requests와 BeautifulSoup을 설치했다.

문제점
-----
      <a href="#" class="title ellipsis" title="재생" onclick="fnPlaySong('89952547','1');return false;">
                                            
                                            
                                            
                                            
                                        
                                        
                                    
                                    WANNABE</a>
                                    
chorme에서 개발자도구를 열어 노래제목이 있는 부분을 확인해보니 엄청난 공백이 있는 것을 확인할 수 있다.
> 구글에 검색해보니 공백을 없애기 위해 .strip()이라는 함수를 BeautifulSoup에서 제공하고있다.

     title = song.find('a', {'class': "title ellipsis"}).text
    singer = song.find('a', {'class': "artist ellipsis"}).text

>구글에 찾아보니 .find()함수에서 딕셔너리를 사용해 원하는 class의 내용만 가져올 수 있었다. 
>.text를 이용해서 text만 추출했다. 

완성본
----
1. WANNABE ITZY (있지)
2. 어떻게 지내 오반
3. 아무노래 지코 (ZICO)
4. 시작 가호 (Gaho)
5. ON 방탄소년단
6. 마음을 드려요 아이유 (IU)
7. METEOR 창모 (CHANGMO)
8. 바빠서 (Feat. 헤이즈) 개코
9. FIESTA IZ*ONE (아이즈원)
10. Blueming 아이유 (IU)
11. 돌덩이 하현우 (국카스텐)
12. 늦은 밤 너의 집 앞 골목길에서 노을
13. 흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야 장범준
14. 그때 그 아인 김필
15. 솔직히 지친다 청하
16. Psycho Red Velvet (레드벨벳)
17. 00:00 (Zero O'Clock) 방탄소년단
18. HIP 마마무(Mamamoo)
19. 다시 난, 여기 백예린
20. 어떤 말도 Crush
21. 어떻게 이별까지 사랑하겠어, 널 사랑하는 거지 AKMU (악동뮤지션)
22. 둘만의 세상으로 가 Crush
23. 오늘도 빛나는 너에게 (To You My Light) (Feat.이라온) 마크툽 (Maktub)
24. 작은 것들을 위한 시 (Boy With Luv) (Feat. Halsey) 방탄소년단
25. Black Swan 방탄소년단
26. 반만 진민호
27. 잘 지내고 있는지 궁금해 V.O.S
28. Love poem 아이유 (IU)
29. 사랑의 인사 씨야 (SeeYa)
30. 친구 방탄소년단
31. 안녕 폴킴
32. PAY DAY (Prod. by GRAY) 창모 (CHANGMO) & ASH ISLAND & 정기고
33. 2002 Anne-Marie
34. Square (2017) 백예린
35. 모든 날, 모든 순간 (Every day, Every Moment) 폴킴
36. 시든 꽃에 물을 주듯 HYNN (박혜원)
37. 어떤 날엔 김재환
38. 조금 취했어 (Prod. by 2soo) 임재현
39. 사랑이란 멜로는 없어 전상근
40. Filter 방탄소년단
41. Memories Maroon 5
42. bad guy Billie Eilish
43. 영웅 (英雄; Kick It) NCT 127
44. 아마두 (Feat. 우원재 & 김효은 & 넉살 & Huckleberry P) 염따 & 딥플로우 & 팔로알토 (Paloalto) & The Quiett & 사이먼 도미닉
45. 다시 만날까 봐 V.O.S
46. Moon 방탄소년단
47. Paris In The Rain Lauv
48. 사랑에 연습이 있었다면 (Prod. by 2soo) 임재현
49. 포장마차 황인욱
50. 사랑이 식었다고 말해도 돼 먼데이 키즈 (Monday Kiz)