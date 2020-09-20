graph [
  node [
    id 0
    label 1
    disk 8
    cpu 1
    memory 14
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
    disk 7
    cpu 1
    memory 8
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 3
    memory 14
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 1
    memory 11
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 121
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 197
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 126
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
    delay 25
    bw 110
  ]
  edge [
    source 3
    target 5
    delay 25
    bw 167
  ]
]
