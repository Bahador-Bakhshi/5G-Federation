graph [
  node [
    id 0
    label 1
    disk 4
    cpu 3
    memory 12
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 1
    memory 11
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 2
    memory 6
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 4
    memory 13
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 4
    memory 13
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 2
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 179
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 198
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 137
  ]
  edge [
    source 0
    target 3
    delay 35
    bw 120
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 70
  ]
  edge [
    source 2
    target 4
    delay 31
    bw 180
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 159
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 151
  ]
]
