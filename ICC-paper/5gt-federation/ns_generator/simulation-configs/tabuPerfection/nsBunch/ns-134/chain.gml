graph [
  node [
    id 0
    label 1
    disk 9
    cpu 3
    memory 4
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 3
    memory 7
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 3
    memory 4
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 2
    memory 8
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 4
    memory 9
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 2
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 125
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 158
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 62
  ]
  edge [
    source 1
    target 3
    delay 25
    bw 115
  ]
  edge [
    source 2
    target 5
    delay 25
    bw 174
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 64
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 167
  ]
]
