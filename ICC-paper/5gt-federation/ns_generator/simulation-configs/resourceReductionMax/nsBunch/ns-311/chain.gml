graph [
  node [
    id 0
    label 1
    disk 7
    cpu 1
    memory 10
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 4
    memory 2
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 1
    memory 12
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 2
    memory 11
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 4
    memory 6
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 1
    memory 7
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 181
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 178
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 121
  ]
  edge [
    source 1
    target 5
    delay 29
    bw 165
  ]
  edge [
    source 2
    target 3
    delay 25
    bw 74
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 59
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 111
  ]
]
