graph [
  node [
    id 0
    label 1
    disk 1
    cpu 2
    memory 9
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 1
    memory 4
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 2
    memory 1
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 1
    memory 12
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 4
    memory 14
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 4
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 62
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 125
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 89
  ]
  edge [
    source 2
    target 3
    delay 26
    bw 102
  ]
  edge [
    source 2
    target 4
    delay 27
    bw 119
  ]
  edge [
    source 3
    target 5
    delay 34
    bw 140
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 167
  ]
]
