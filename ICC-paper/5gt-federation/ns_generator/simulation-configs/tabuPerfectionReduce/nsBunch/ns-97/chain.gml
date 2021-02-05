graph [
  node [
    id 0
    label 1
    disk 4
    cpu 3
    memory 6
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 2
    memory 8
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 2
    memory 10
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 3
    memory 6
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 1
    memory 6
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 1
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 59
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 153
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 62
  ]
  edge [
    source 0
    target 3
    delay 25
    bw 79
  ]
  edge [
    source 1
    target 4
    delay 35
    bw 156
  ]
  edge [
    source 3
    target 5
    delay 29
    bw 199
  ]
]
