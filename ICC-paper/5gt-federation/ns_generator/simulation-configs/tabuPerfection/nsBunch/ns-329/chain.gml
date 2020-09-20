graph [
  node [
    id 0
    label 1
    disk 7
    cpu 1
    memory 7
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 3
    memory 15
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 4
    memory 3
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 6
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 3
    memory 10
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 1
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 152
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 94
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 65
  ]
  edge [
    source 0
    target 3
    delay 25
    bw 100
  ]
  edge [
    source 1
    target 5
    delay 32
    bw 98
  ]
  edge [
    source 2
    target 4
    delay 35
    bw 158
  ]
  edge [
    source 3
    target 5
    delay 31
    bw 134
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 88
  ]
]
