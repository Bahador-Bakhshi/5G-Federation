graph [
  node [
    id 0
    label 1
    disk 1
    cpu 1
    memory 16
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 2
    memory 15
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 4
    memory 6
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 3
    memory 9
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 2
    memory 13
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 4
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 118
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 58
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 106
  ]
  edge [
    source 0
    target 3
    delay 25
    bw 150
  ]
  edge [
    source 1
    target 4
    delay 35
    bw 154
  ]
  edge [
    source 2
    target 5
    delay 29
    bw 78
  ]
  edge [
    source 3
    target 5
    delay 25
    bw 169
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 118
  ]
]
