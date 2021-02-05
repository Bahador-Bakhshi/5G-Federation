graph [
  node [
    id 0
    label 1
    disk 10
    cpu 4
    memory 13
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 3
    memory 10
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 3
    memory 8
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 2
    memory 3
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 3
    memory 11
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 2
    memory 3
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 109
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 199
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 172
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 149
  ]
  edge [
    source 2
    target 4
    delay 33
    bw 115
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 95
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 50
  ]
]
