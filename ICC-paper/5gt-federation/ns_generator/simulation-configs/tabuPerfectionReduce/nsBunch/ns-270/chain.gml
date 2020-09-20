graph [
  node [
    id 0
    label 1
    disk 10
    cpu 1
    memory 15
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 2
    memory 5
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 2
    memory 12
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 1
    memory 4
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 2
    memory 4
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 3
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 155
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 62
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 85
  ]
  edge [
    source 1
    target 3
    delay 27
    bw 160
  ]
  edge [
    source 2
    target 3
    delay 35
    bw 151
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 88
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 198
  ]
]
